### header to add
drop database if exists iptvm;
create database iptvm default character set utf8 collate utf8_general_ci;
use iptvm;

.......
.......

### footer to add(scheduler event)

# scheduler event
SET GLOBAL event_scheduler = 1;
DROP EVENT IF EXISTS callUpdateProcedure;
DELIMITER ;;
CREATE EVENT callUpdateProcedure ON SCHEDULE EVERY 1 SECOND STARTS CURRENT_TIMESTAMP ON COMPLETION NOT PRESERVE ENABLE DO CALL updateServerState
;;
DELIMITER ;