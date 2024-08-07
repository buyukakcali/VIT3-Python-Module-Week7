DELIMITER //

CREATE TRIGGER trg_after_insert_form_data
AFTER INSERT ON form_data
FOR EACH ROW
BEGIN
    DECLARE applicantID INT;
    DECLARE newID INT;
    
    -- Applicant control via email
    SELECT ID INTO applicantID FROM form_basvuran WHERE Email = NEW.Email LIMIT 1;
    
    -- If there is no applicant
    IF applicantID IS NULL THEN
    -- Add new applicant
        INSERT INTO form_basvuran (ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet)
        VALUES (NEW.ZamanDamgasi, NEW.Ad, NEW.Soyad, NEW.Email, NEW.Telefon, NEW.PostaKodu, NEW.YasadiginizEyalet);
        SET applicantID = LAST_INSERT_ID();        
        -- Add log
		INSERT INTO trigger_logs (log_message, log_time) VALUES ('New applicant is added to form_basvuran table', NEW.ZamanDamgasi);
        
        -- Add new application
        INSERT INTO form_basvuru (BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir)
        VALUES (applicantID, NEW.ZamanDamgasi, NEW.BasvuruDonemi, NEW.SuAnkiDurum, NEW.ITPHEgitimKatilmak, NEW.EkonomikDurum, NEW.DilKursunaDevam, NEW.IngilizceSeviye, NEW.HollandacaSeviye, NEW.BaskiGoruyor, NEW.BootcampBitirdi, NEW.OnlineITKursu, NEW.ITTecrube, NEW.ProjeDahil, NEW.CalismakIstedigi, NEW.NedenKatilmakIstiyor, NEW.MotivasyonunNedir);
        -- Add log
		INSERT INTO trigger_logs (log_message, log_time) VALUES ('New application is added to form_basvuru table', NEW.ZamanDamgasi);
    ELSE
        -- <<< Buradaki ELSE in altinda basvuran bilgileri guncellenecek! >>> --
        -- Burasi en karmasik isi yapan bolum. Eger kisi birkac gun sonra ayni mail adresiyle basvurusunu 
		-- guncellemek isterse de calisiyor. Drivedaki satir sayisi artsa da form_data daki satir sayisi 
		-- artmiyor. sadece guncelleniyor.        
		-- >> Check the applicant's data and update if there are any changes
        IF (SELECT Ad FROM form_basvuran WHERE ID = applicantID) <> NEW.Ad OR
           (SELECT Soyad FROM form_basvuran WHERE ID = applicantID) <> NEW.Soyad OR
           (SELECT Telefon FROM form_basvuran WHERE ID = applicantID) <> NEW.Telefon OR
           (SELECT PostaKodu FROM form_basvuran WHERE ID = applicantID) <> NEW.PostaKodu OR
           (SELECT YasadiginizEyalet FROM form_basvuran WHERE ID = applicantID) <> NEW.YasadiginizEyalet THEN
           
			INSERT INTO form_old_basvuran (ID_in_basvuranTable, NeZamanGuncellendi, ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet)
            SELECT ID, NEW.ZamanDamgasi, ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet
            FROM form_basvuran
            WHERE ID = applicantID;
            
            UPDATE form_basvuran
            SET ZamanDamgasi = NEW.ZamanDamgasi, Ad = NEW.Ad, Soyad = NEW.Soyad, Telefon = NEW.Telefon, PostaKodu = NEW.PostaKodu, YasadiginizEyalet = NEW.YasadiginizEyalet
            WHERE ID = applicantID;            
            -- Add log
            INSERT INTO trigger_logs (log_message, log_time) VALUES ('(WITH NEW FORM FILLING) Basvuran information is updated "in trg_after_insert_data"', NEW.ZamanDamgasi);
        END IF;
        -- <<< -------------------------- >>> --
        
        -- Application period control and addition/update
        SELECT ID INTO newID FROM form_basvuru WHERE BasvuranID = applicantID AND BasvuruDonemi = NEW.BasvuruDonemi LIMIT 1;        
        IF newID IS NULL THEN
            INSERT INTO form_basvuru (BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir)
            VALUES (applicantID, NEW.ZamanDamgasi, NEW.BasvuruDonemi, NEW.SuAnkiDurum, NEW.ITPHEgitimKatilmak, NEW.EkonomikDurum, NEW.DilKursunaDevam, NEW.IngilizceSeviye, NEW.HollandacaSeviye, NEW.BaskiGoruyor, NEW.BootcampBitirdi, NEW.OnlineITKursu, NEW.ITTecrube, NEW.ProjeDahil, NEW.CalismakIstedigi, NEW.NedenKatilmakIstiyor, NEW.MotivasyonunNedir);
            -- Add log
            INSERT INTO trigger_logs (log_message, log_time) VALUES ('New application of existing applicant is added to form_basvuru table', NEW.ZamanDamgasi);
        ELSE
			-- <<< Buradaki ELSE in altinda BASVURU bilgileri guncellenecek! >>> --
			-- Burasi en karmasik isi yapan bolum. Eger kisi birkac gun sonra ayni mail adresiyle basvurusunu 
			-- guncellemek isterse de calisiyor. Drivedaki satir sayisi artsa da form_data daki satir sayisi 
			-- artmiyor. sadece guncelleniyor.   
        	-- >> Check the application's data and update if there are any changes
			IF (SELECT SuAnkiDurum FROM form_basvuru WHERE ID = newID) <> NEW.SuAnkiDurum OR
            (SELECT ITPHEgitimKatilmak FROM form_basvuru WHERE ID = newID) <> NEW.ITPHEgitimKatilmak OR
            (SELECT EkonomikDurum FROM form_basvuru WHERE ID = newID) <> NEW.EkonomikDurum OR
            (SELECT DilKursunaDevam FROM form_basvuru WHERE ID = newID) <> NEW.DilKursunaDevam OR
            (SELECT IngilizceSeviye FROM form_basvuru WHERE ID = newID) <> NEW.IngilizceSeviye OR
            (SELECT HollandacaSeviye FROM form_basvuru WHERE ID = newID) <> NEW.HollandacaSeviye OR
            (SELECT BaskiGoruyor FROM form_basvuru WHERE ID = newID) <> NEW.BaskiGoruyor OR
            (SELECT BootcampBitirdi FROM form_basvuru WHERE ID = newID) <> NEW.BootcampBitirdi OR
            (SELECT OnlineITKursu FROM form_basvuru WHERE ID = newID) <> NEW.OnlineITKursu OR
            (SELECT ITTecrube FROM form_basvuru WHERE ID = newID) <> NEW.ITTecrube OR
            (SELECT ProjeDahil FROM form_basvuru WHERE ID = newID) <> NEW.ProjeDahil OR
            (SELECT CalismakIstedigi FROM form_basvuru WHERE ID = newID) <> NEW.CalismakIstedigi OR
            (SELECT NedenKatilmakIstiyor FROM form_basvuru WHERE ID = newID) <> NEW.NedenKatilmakIstiyor OR
            (SELECT MotivasyonunNedir FROM form_basvuru WHERE ID = newID) <> NEW.MotivasyonunNedir THEN	-- buraya diger sutunlarin kontrolleri gelecek
				INSERT INTO form_old_basvuru (ID_in_basvuruTable, NeZamanGuncellendi, BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir, IlkMulakat, IkinciMulakat)
				SELECT ID, NEW.ZamanDamgasi, BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir, IlkMulakat, IkinciMulakat
				FROM form_basvuru
				WHERE ID = newID;
					
				UPDATE form_basvuru
				SET ZamanDamgasi = NEW.ZamanDamgasi, SuAnkiDurum = NEW.SuAnkiDurum, ITPHEgitimKatilmak = NEW.ITPHEgitimKatilmak, EkonomikDurum = NEW.EkonomikDurum, DilKursunaDevam = NEW.DilKursunaDevam, IngilizceSeviye = NEW.IngilizceSeviye, HollandacaSeviye = NEW.HollandacaSeviye, BaskiGoruyor = NEW.BaskiGoruyor, BootcampBitirdi = NEW.BootcampBitirdi, OnlineITKursu = NEW.OnlineITKursu, ITTecrube = NEW.ITTecrube, ProjeDahil = NEW.ProjeDahil, CalismakIstedigi = NEW.CalismakIstedigi, NedenKatilmakIstiyor = NEW.NedenKatilmakIstiyor, MotivasyonunNedir = NEW.MotivasyonunNedir
				WHERE ID = newID;
				-- Add log
				INSERT INTO trigger_logs (log_message, log_time) VALUES ('(WITH NEW FORM FILLING) Basvuru information is updated "in trg_after_insert_data"', NEW.ZamanDamgasi);
			END IF;
            -- <<< -------------------------- >>> --
            
        END IF;
    END IF;
    -- Add log to verify that the trigger worked
    INSERT INTO trigger_logs (log_message, log_time) VALUES ('trg_after_insert_form_data trigger is executed', NEW.ZamanDamgasi);
END//

DELIMITER ;



DELIMITER //

CREATE TRIGGER trg_after_update_form_data
AFTER UPDATE ON form_data
FOR EACH ROW
BEGIN
    DECLARE applicantID INT;
    DECLARE newID INT;
    
    -- Applicant control via email
    SELECT ID INTO applicantID FROM form_basvuran WHERE Email = NEW.Email LIMIT 1;
    
    -- If there is no applicant, he/she is POSSIBLY changing his/her email address. (Expected to be rare), add log and update applicant information
    IF applicantID IS NULL THEN    
		-- ******************* --
        
		-- CHECK FROM OLD EMAIL
        SELECT ID INTO applicantID FROM form_basvuran WHERE Email = OLD.Email LIMIT 1;
        
        -- (OLD) Check the applicant's data and update if there are any changes
        IF (SELECT Ad FROM form_basvuran WHERE ID = applicantID) <> NEW.Ad OR
           (SELECT Soyad FROM form_basvuran WHERE ID = applicantID) <> NEW.Soyad OR
           (SELECT Email FROM form_basvuran WHERE ID = applicantID) <> NEW.Email OR
           (SELECT Telefon FROM form_basvuran WHERE ID = applicantID) <> NEW.Telefon OR
           (SELECT PostaKodu FROM form_basvuran WHERE ID = applicantID) <> NEW.PostaKodu OR
           (SELECT YasadiginizEyalet FROM form_basvuran WHERE ID = applicantID) <> NEW.YasadiginizEyalet THEN
           
            INSERT INTO form_old_basvuran (ID_in_basvuranTable, NeZamanGuncellendi, ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet)
            SELECT ID, NEW.ZamanDamgasi, ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet
            FROM form_basvuran
            WHERE ID = applicantID;
            
            UPDATE form_basvuran
            SET ZamanDamgasi = NEW.ZamanDamgasi, Ad = NEW.Ad, Soyad = NEW.Soyad, Email = NEW.Email, Telefon = NEW.Telefon, PostaKodu = NEW.PostaKodu, YasadiginizEyalet = NEW.YasadiginizEyalet
            WHERE ID = applicantID;
            -- (OLD) Add log
            INSERT INTO trigger_logs (log_message, log_time) VALUES ('(OLD) Basvuru information (including email address) is updated "in trg_after_update_form_data"', NEW.ZamanDamgasi);
		ELSE
            INSERT INTO trigger_logs (log_message, log_time)
            VALUES (CONCAT('(OLD) It means there is an error right now that I don\'t know why... ("in trg_after_update_form_data") Line Number: ', (SELECT RowID FROM form_data WHERE Email = OLD.Email)), NEW.ZamanDamgasi);
		END IF;
        
        -- (OLD) Application period control and addition/update
        SELECT ID INTO newID FROM form_basvuru WHERE BasvuranID = applicantID AND BasvuruDonemi = NEW.BasvuruDonemi;    
        IF newID IS NULL THEN        
            -- (OLD) Add log
            INSERT INTO trigger_logs (log_message, log_time) VALUES ('(OLD) Unexpected code situation! This code shuldn\'t be executed... ("in trg_after_update_form_data")', NEW.ZamanDamgasi);
        ELSE
            -- (OLD) Check the application's data and update if there are any changes
			IF (SELECT SuAnkiDurum FROM form_basvuru WHERE ID = newID) <> NEW.SuAnkiDurum OR
            (SELECT ITPHEgitimKatilmak FROM form_basvuru WHERE ID = newID) <> NEW.ITPHEgitimKatilmak OR
            (SELECT EkonomikDurum FROM form_basvuru WHERE ID = newID) <> NEW.EkonomikDurum OR
            (SELECT DilKursunaDevam FROM form_basvuru WHERE ID = newID) <> NEW.DilKursunaDevam OR
            (SELECT IngilizceSeviye FROM form_basvuru WHERE ID = newID) <> NEW.IngilizceSeviye OR
            (SELECT HollandacaSeviye FROM form_basvuru WHERE ID = newID) <> NEW.HollandacaSeviye OR
            (SELECT BaskiGoruyor FROM form_basvuru WHERE ID = newID) <> NEW.BaskiGoruyor OR
            (SELECT BootcampBitirdi FROM form_basvuru WHERE ID = newID) <> NEW.BootcampBitirdi OR
            (SELECT OnlineITKursu FROM form_basvuru WHERE ID = newID) <> NEW.OnlineITKursu OR
            (SELECT ITTecrube FROM form_basvuru WHERE ID = newID) <> NEW.ITTecrube OR
            (SELECT ProjeDahil FROM form_basvuru WHERE ID = newID) <> NEW.ProjeDahil OR
            (SELECT CalismakIstedigi FROM form_basvuru WHERE ID = newID) <> NEW.CalismakIstedigi OR
            (SELECT NedenKatilmakIstiyor FROM form_basvuru WHERE ID = newID) <> NEW.NedenKatilmakIstiyor OR
            (SELECT MotivasyonunNedir FROM form_basvuru WHERE ID = newID) <> NEW.MotivasyonunNedir THEN
				INSERT INTO form_old_basvuru (ID_in_basvuruTable, NeZamanGuncellendi, BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir, IlkMulakat, IkinciMulakat)
				SELECT ID, NEW.ZamanDamgasi, BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir, IlkMulakat, IkinciMulakat
				FROM form_basvuru
				WHERE ID = newID;
					
				UPDATE form_basvuru
				SET ZamanDamgasi = NEW.ZamanDamgasi, SuAnkiDurum = NEW.SuAnkiDurum, ITPHEgitimKatilmak = NEW.ITPHEgitimKatilmak, EkonomikDurum = NEW.EkonomikDurum, DilKursunaDevam = NEW.DilKursunaDevam, IngilizceSeviye = NEW.IngilizceSeviye, HollandacaSeviye = NEW.HollandacaSeviye, BaskiGoruyor = NEW.BaskiGoruyor, BootcampBitirdi = NEW.BootcampBitirdi, OnlineITKursu = NEW.OnlineITKursu, ITTecrube = NEW.ITTecrube, ProjeDahil = NEW.ProjeDahil, CalismakIstedigi = NEW.CalismakIstedigi, NedenKatilmakIstiyor = NEW.NedenKatilmakIstiyor, MotivasyonunNedir = NEW.MotivasyonunNedir
				WHERE ID = newID;
				-- (OLD) Add log
				INSERT INTO trigger_logs (log_message, log_time) VALUES ('(OLD) Basvuru information is updated "in trg_after_update_form_data"', NEW.ZamanDamgasi);
			END IF;
        END IF;        
        -- ******************* --
        
    ELSE
        -- Check the applicant's data and update if there are any changes
        IF (SELECT Ad FROM form_basvuran WHERE ID = applicantID) <> NEW.Ad OR
           (SELECT Soyad FROM form_basvuran WHERE ID = applicantID) <> NEW.Soyad OR
           (SELECT Telefon FROM form_basvuran WHERE ID = applicantID) <> NEW.Telefon OR
           (SELECT PostaKodu FROM form_basvuran WHERE ID = applicantID) <> NEW.PostaKodu OR
           (SELECT YasadiginizEyalet FROM form_basvuran WHERE ID = applicantID) <> NEW.YasadiginizEyalet THEN
           
            INSERT INTO form_old_basvuran (ID_in_basvuranTable, NeZamanGuncellendi, ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet)
            SELECT ID, NEW.ZamanDamgasi, ZamanDamgasi, Ad, Soyad, Email, Telefon, PostaKodu, YasadiginizEyalet
            FROM form_basvuran
            WHERE ID = applicantID;
            
            UPDATE form_basvuran
            SET ZamanDamgasi = NEW.ZamanDamgasi, Ad = NEW.Ad, Soyad = NEW.Soyad, Telefon = NEW.Telefon, PostaKodu = NEW.PostaKodu, YasadiginizEyalet = NEW.YasadiginizEyalet
            WHERE ID = applicantID;           
            -- Add log
            INSERT INTO trigger_logs (log_message, log_time) VALUES ('Basvuran information is updated "in trg_after_update_form_data"', NEW.ZamanDamgasi);
        END IF;

        -- Application period control and addition/update
        SELECT ID INTO newID FROM form_basvuru WHERE BasvuranID = applicantID AND BasvuruDonemi = NEW.BasvuruDonemi;
        IF newID IS NULL THEN        
            -- Add log
            INSERT INTO trigger_logs (log_message, log_time) VALUES ('Unexpected code situation! This code shuldn\'t be executed... ("in trg_after_update_form_data")', NEW.ZamanDamgasi);
        ELSE
            -- Check the application's data and update if there are any changes
			IF (SELECT SuAnkiDurum FROM form_basvuru WHERE ID = newID) <> NEW.SuAnkiDurum OR
            (SELECT ITPHEgitimKatilmak FROM form_basvuru WHERE ID = newID) <> NEW.ITPHEgitimKatilmak OR
            (SELECT EkonomikDurum FROM form_basvuru WHERE ID = newID) <> NEW.EkonomikDurum OR
            (SELECT DilKursunaDevam FROM form_basvuru WHERE ID = newID) <> NEW.DilKursunaDevam OR
            (SELECT IngilizceSeviye FROM form_basvuru WHERE ID = newID) <> NEW.IngilizceSeviye OR
            (SELECT HollandacaSeviye FROM form_basvuru WHERE ID = newID) <> NEW.HollandacaSeviye OR
            (SELECT BaskiGoruyor FROM form_basvuru WHERE ID = newID) <> NEW.BaskiGoruyor OR
            (SELECT BootcampBitirdi FROM form_basvuru WHERE ID = newID) <> NEW.BootcampBitirdi OR
            (SELECT OnlineITKursu FROM form_basvuru WHERE ID = newID) <> NEW.OnlineITKursu OR
            (SELECT ITTecrube FROM form_basvuru WHERE ID = newID) <> NEW.ITTecrube OR
            (SELECT ProjeDahil FROM form_basvuru WHERE ID = newID) <> NEW.ProjeDahil OR
            (SELECT CalismakIstedigi FROM form_basvuru WHERE ID = newID) <> NEW.CalismakIstedigi OR
            (SELECT NedenKatilmakIstiyor FROM form_basvuru WHERE ID = newID) <> NEW.NedenKatilmakIstiyor OR
            (SELECT MotivasyonunNedir FROM form_basvuru WHERE ID = newID) <> NEW.MotivasyonunNedir THEN
				INSERT INTO form_old_basvuru (ID_in_basvuruTable, NeZamanGuncellendi, BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir, IlkMulakat, IkinciMulakat)
				SELECT ID, NEW.ZamanDamgasi, BasvuranID, ZamanDamgasi, BasvuruDonemi, SuAnkiDurum, ITPHEgitimKatilmak, EkonomikDurum, DilKursunaDevam, IngilizceSeviye, HollandacaSeviye, BaskiGoruyor, BootcampBitirdi, OnlineITKursu, ITTecrube, ProjeDahil, CalismakIstedigi, NedenKatilmakIstiyor, MotivasyonunNedir, IlkMulakat, IkinciMulakat
				FROM form_basvuru
				WHERE ID = newID;
					
				UPDATE form_basvuru
				SET ZamanDamgasi = NEW.ZamanDamgasi, SuAnkiDurum = NEW.SuAnkiDurum, ITPHEgitimKatilmak = NEW.ITPHEgitimKatilmak, EkonomikDurum = NEW.EkonomikDurum, DilKursunaDevam = NEW.DilKursunaDevam, IngilizceSeviye = NEW.IngilizceSeviye, HollandacaSeviye = NEW.HollandacaSeviye, BaskiGoruyor = NEW.BaskiGoruyor, BootcampBitirdi = NEW.BootcampBitirdi, OnlineITKursu = NEW.OnlineITKursu, ITTecrube = NEW.ITTecrube, ProjeDahil = NEW.ProjeDahil, CalismakIstedigi = NEW.CalismakIstedigi, NedenKatilmakIstiyor = NEW.NedenKatilmakIstiyor, MotivasyonunNedir = NEW.MotivasyonunNedir
				WHERE ID = newID;
				-- Add log
				INSERT INTO trigger_logs (log_message, log_time) VALUES ('Basvuru information is updated "in trg_after_update_form_data"', NEW.ZamanDamgasi);
			END IF;
        END IF;
    END IF;    
    -- Add log to verify that the trigger worked
    INSERT INTO trigger_logs (log_message, log_time) VALUES ('trg_after_update_form_data tigger is executed', NEW.ZamanDamgasi);
END//

DELIMITER ;