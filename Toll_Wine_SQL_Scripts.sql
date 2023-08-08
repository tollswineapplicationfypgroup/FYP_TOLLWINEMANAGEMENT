-- --------------------------------------------------------
-- Host:                         us-cdbr-east-06.cleardb.net
-- Server version:               5.6.50-log - MySQL Community Server (GPL)
-- Server OS:                    Linux
-- HeidiSQL Version:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping data for table heroku_eb7517145b609d1.employee: ~2 rows (approximately)
INSERT INTO `employee` (`employee_id`, `apikey`, `email`, `first_name`, `last_name`, `password`, `phone_number`, `pic`, `role`, `username`) VALUES
	(1, '', 'TShelby@toll.com', 'Thomas', 'Shelby', '$2a$12$mPG0LpgqBp2DquVtU1aXEu4uALE1oiwIHnjxwA4E3o.1D13djlAdi', 97858875, 'TommyShelby.jpeg', 'ROLE_ADMIN', 'TS2000'),
	(4, 'e86debef26bdacebfca2f2769853cfb07fd75a04ae5f41', 'ashrafkhan@toll.com', 'Ashraf', 'Khan', '$2a$10$FOl12y6V6lyVkQTj0rvmx.xl.pb3RAyi6rRoDic9XT/CYSbAIK4pC', 91056998, 'sad_boy.jpg', 'ROLE_USER', 'AshyKhan');

-- Dumping data for table heroku_eb7517145b609d1.inbound_list: ~3 rows (approximately)
INSERT INTO `inbound_list` (`id`, `arrival_date`, `completed_date`, `current_date_and_time`, `departure_date`, `exporter`, `handling_agent`, `importer`, `is_doing`, `permit_no`, `status_completed`, `t_cartons`, `t_quantity`) VALUES
	(123456789, '2023-07-14', NULL, '2023-08-08 14:12:34.816983', '2023-07-17', 'NTUC', 'None', 'Wine Lovers Inc', NULL, '2023WINE123', b'1', 5, 22),
	(693826083, '2023-08-21', NULL, '2023-08-08 14:13:06.362186', '2023-08-30', '7-Eleven', 'Ashraf', 'Cellar Door Wines', 1, '2023EXPORT789', b'0', 5, 24),
	(819074012, '2023-07-17', NULL, '2023-08-08 14:12:49.557656', '2023-07-20', 'Cold Storage', 'None', 'Vino Imports Co.', NULL, '2023IMPORT456', b'0', 5, 24);

-- Dumping data for table heroku_eb7517145b609d1.report: ~2 rows (approximately)
INSERT INTO `report` (`report_id`, `date_created`, `description`, `report_title`, `report_type`, `status`, `employee_id`, `inbound_list_id`, `wine_label_id`) VALUES
	(4, '2023-08-08', 'I have accidentally broken the bottle as it was kind of slippery... please dont fire me...', 'Broken Bottle', 'Broken Bottle', 'Completed', 4, 693826083, 146604),
	(14, '2023-08-08', 'Been Looking for the bottle around the crate but it seems like its missing', 'Missing Bottle', 'Others', 'Pending', 4, 693826083, 245427);

-- Dumping data for table heroku_eb7517145b609d1.wine_label: ~15 rows (approximately)
INSERT INTO `wine_label` (`id`, `alcohol_content`, `bottle_information`, `brand_name`, `current_date_and_time`, `grape_variety`, `importer_information`, `model_name`, `quantity`, `region_of_production`, `status_completed`, `vintage`, `wine_name`, `inbound_list_id`) VALUES
	(137464, 0.11, '750ml', 'Valdo', '2023-08-08 14:12:50.831174', 'Glera,Pinot Noir ; Champagne & Sparkling', 'Vino Imports Co.', 'OP-PRB-NV-2021', 6, 'Italy ; Veneto ', b'0', 2021, 'Oro Puro Prosecco Rosé Brut N.V', 819074012),
	(146604, 0.12, '750ml', 'CASA DEFRÀ', '2023-08-08 14:13:06.616282', 'Pinot Grigio', 'Cellar Door Wines', 'PGDV-DOC-2022', 6, 'Italy ; Veneto', b'1', 2022, 'Pinot Grigio delle Venezie DOC', 693826083),
	(245427, 0.13, '750ml ', 'Calabria Family Wines ', '2023-08-08 14:13:07.640742', 'Chardonnay ; White wine', 'Cellar Door Wines', 'CFW-RICH-2-2021', 2, 'Australia', b'1', 2021, 'CALABRIA FAMILY WINES "Richland"', 693826083),
	(272904, 0.13, '750ml', 'Calabria Family', '2023-08-08 14:12:35.601954', 'Chardonnay ; white wine', 'Wine Lovers Inc', 'WOLF-RIESLING-2021', 4, 'Australia ; Riverina', b'1', 2021, 'Calabria Family Wines "Richland" Chardonnay', 123456789),
	(294477, 0.13, '750ml ', 'DOMAINE SIOUVETTE', '2023-08-08 14:12:50.576941', 'Côtes de Provence', 'Vino Imports Co.', 'LEXC-2021', 8, 'France ', b'0', 2021, 'L\' Exception', 819074012),
	(351492, 0.125, '750ml', 'Vignobles Vellas', '2023-08-08 14:13:07.384087', 'Merlot, Syrah ; Rose wine', 'Cellar Door Wines', 'PLDR-2021', 6, 'France', b'1', 2021, 'Pays d\'Oc IGP ; The power of Love Rose', 693826083),
	(688996, 0.15, '750ml ', '7 DEADLY WINE', '2023-08-08 14:12:50.321989', 'Zinfandel ; Red wine', 'Vino Imports Co.', '7DZ-2018', 4, 'California', b'0', 2018, '7 Deadly Zins', 819074012),
	(807064, 0.135, '1500ml ; 1.5L ', 'Baron De Ley', '2023-08-08 14:12:36.111539', 'Tempranillo ; red wine ', 'Wine Lovers Inc', 'BDL-RIOJA-MAG-RES-2016', 4, 'Spain ; Rioja ', b'1', 2016, 'Baron De Ley Magnum Rioja Reserva ', 123456789),
	(842123, 0.15, '750ml', 'Domaine Les Tailhades', '2023-08-08 14:12:35.345664', 'Muscat ; white wine', 'Wine Lovers Inc', 'LTD-TAIL-MUSCAT-2020', 2, 'France ; Languedoc ', b'1', 2020, 'DOMAINE LES TAILHADES "Petit Grains" Muscat De Saint-Jean De Minervois', 123456789),
	(873367, 0.11, '750ml ', 'CASA DEFRÀ', '2023-08-08 14:13:07.129186', 'Glera ; Champagne & Sparkling ', 'Cellar Door Wines', 'CDF-PROS-DOC-2023', 4, 'Italy ; Veneto', b'0', 2023, 'CASA DE FRÀ Prosecco DOC ', 693826083),
	(887909, 0.135, '750ml', 'ALMA MORA', '2023-08-08 14:13:06.874756', 'Malbec ; Red Wine ', 'Cellar Door Wines', 'MR-RES-2020', 6, 'Argentina', b'0', 2020, 'Malbec Reserva', 693826083),
	(894133, 0.12, '750ml ', 'BISCARDO', '2023-08-08 14:12:50.067975', 'Pinot Nero ; Rose wine', 'Vino Imports Co.', 'BISC-RP-2021', 4, 'Italy ; Veneto ', b'0', 2021, 'Biscardo \'Rosapasso\' ', 819074012),
	(894979, 0.13, '750ml', 'BRUCE JACK ', '2023-08-08 14:12:49.813523', 'Chenin Blanc ; White wine ', 'Vino Imports Co.', 'BJ-CB-2022', 2, 'South Africa ; Western Cape', b'0', 2022, 'Bruce Jack Chenin Blanc', 819074012),
	(925981, 0.145, '750ml', 'Castle Rock ', '2023-08-08 14:12:35.090714', 'Cabernet Sauvignon ; red wine ', 'Wine Lovers Inc', 'CRCS-CABRES-2017', 6, 'USA ; Napa Valley ', b'1', 2017, 'Castle Rock "Reserve" Cabernet Sauvignon', 123456789),
	(955281, 0.123, '750ml', 'Woldberger', '2023-08-08 14:12:35.856927', 'Riesling ; white wine ', 'Wine Lovers Inc', 'CFW-RICH-CHARD-2021', 6, 'France ; Alsace', b'1', 2021, 'Wolfberger Riesling', 123456789);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
