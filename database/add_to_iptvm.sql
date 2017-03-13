### header to add
drop database if exists iptvm;
create database iptvm default character set utf8 collate utf8_general_ci;
use iptvm;

.......
.......

### footer to add(trigger and scheduler event)


# trigger
DROP TRIGGER IF EXISTS `insertApp`;
DELIMITER $$
CREATE TRIGGER `insertApp` 
AFTER INSERT ON `server` 
FOR EACH ROW 
BEGIN
insert into mysql values (1, new.serverName );
insert into nginx values (1, new.serverName );
END
$$
DELIMITER ;

# scheduler event
SET GLOBAL event_scheduler = 1;
DROP EVENT IF EXISTS `callUpdateProcedure`;
DELIMITER $$
CREATE EVENT `callUpdateProcedure` ON SCHEDULE EVERY 1 SECOND STARTS CURRENT_TIMESTAMP ON COMPLETION NOT PRESERVE ENABLE DO CALL updateServerState
$$
