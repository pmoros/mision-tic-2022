-- --------------------------------------------------------
-- Host:                         ec2-54-211-255-161.compute-1.amazonaws.com
-- Versión del servidor:         PostgreSQL 14.2 (Ubuntu 14.2-1.pgdg20.04+1+b1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0, 64-bit
-- SO del servidor:              
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla public.city: -1 rows
/*!40000 ALTER TABLE "city" DISABLE KEYS */;
INSERT INTO "city" ("id", "name", "population") VALUES
	(1, 'Bogotá', 7715778),
	(2, 'Medellín', 2490164),
	(3, 'Cali', 2205680),
	(4, 'Barranquilla', 1273646),
	(5, 'Cartagena', 914552),
	(6, 'Cúcuta', 748948),
	(7, 'Soacha', 749034),
	(8, 'Soledad', 664141),
	(9, 'Bucaramanga', 597316),
	(10, 'Bello', 536427),
	(11, 'Villavicencio', 502047),
	(12, 'Ibagué', 501991),
	(13, 'SantaMarta', 484025),
	(14, 'Valledupar', 468165),
	(15, 'Montería', 395184),
	(16, 'Pereira', 399283),
	(17, 'Manizales', 420933),
	(18, 'Pasto', 305360),
	(19, 'Neiva', 340512),
	(20, 'Palmira', 279465),
	(21, 'Popayán', 267389),
	(22, 'Buenaventura', 238648),
	(23, 'Floridablanca', 295724),
	(24, 'Armenia', 297052),
	(25, 'Sincelejo', 259435),
	(26, 'Itagüí', 265527),
	(27, 'Tumaco', 86614),
	(28, 'Envigado', 234143),
	(29, 'Dosquebradas', 213520),
	(30, 'Tuluá', 178030),
	(31, 'Barrancabermeja', 183730),
	(32, 'Riohacha', 147244),
	(33, 'Uribia', 8989),
	(34, 'Maicao', 118889),
	(35, 'Piedecuesta', 150483),
	(36, 'Tunja', 171461),
	(37, 'Yopal', 152421),
	(38, 'Florencia', 152536),
	(39, 'Girón', 152582),
	(40, 'Jamundí', 130114),
	(41, 'Facatativá', 145080),
	(42, 'Fusagasugá', 132633),
	(43, 'Mosquera', 148715),
	(44, 'Chía', 124309),
	(45, 'Zipaquirá', 121962),
	(46, 'Rionegro', 90256),
	(47, 'Magangué', 96380),
	(48, 'Malambo', 130135),
	(49, 'Cartago', 132653),
	(50, 'Sogamoso', 116031),
	(51, 'Quibdó', 112380),
	(52, 'Turbo', 52453),
	(53, 'Ocaña', 116232),
	(54, 'Buga', 109753),
	(55, 'Pitalito', 75434),
	(56, 'Apartadó', 107271),
	(57, 'Madrid', 120823),
	(58, 'Duitama', 112308),
	(59, 'Ciénaga', 110303),
	(60, 'Aguachica', 103209),
	(61, 'Ipiales', 77042),
	(62, 'Lorica', 54430),
	(63, 'Turbaco', 103755),
	(64, 'SantanderdeQuilichao', 52684),
	(65, 'VilladelRosario', 107991),
	(66, 'Sahagún', 53973),
	(67, 'Yumbo', 95072),
	(68, 'Girardot', 105896),
	(69, 'Cereté', 60220),
	(70, 'Funza', 103270),
	(71, 'Sabanalarga', 74713);
/*!40000 ALTER TABLE "city" ENABLE KEYS */;

-- Volcando datos para la tabla public.product_line: -1 rows
/*!40000 ALTER TABLE "product_line" DISABLE KEYS */;
INSERT INTO "product_line" ("id", "name", "description") VALUES
	(1, 'Frutas', ' '),
	(2, 'Hortalizas', ' '),
	(3, 'Huevos', ' '),
	(4, 'Lácteos', ' '),
	(5, 'Plátanos', ' '),
	(6, 'Procesados', ' '),
	(7, 'Tubérculos', ' '),
	(8, 'Vegetales', ' '),
	(9, 'Verduras', ' ');

INSERT INTO "store" ("id", "name", "county", "city_id") VALUES
	(1, 'Mercado Campesino Bogotá', 'Vereda Chorrillos', 1),
	(2, 'Mercado Campesino Medellín', 'Vereda El Jardin', 2),
	(3, 'Mercado Campesino Cali', 'Corregimiento de Pance', 3),
	(4, 'Mercado Campesino Barranquilla', 'Vereda El Peñal', 4),
	(5, 'Mercado Campesino Cúcuta', 'Vereda la Camilandia', 6),
	(6, 'Mercado Campesino Soacha', 'Vereda EL Romeral', 7),
	(7, 'Mercado Campesino Villavicencio', 'Vereda El Carmen', 11),
	(8, 'Mercado Campesino Ibagué', 'Vereda La Maria', 12);
/*!40000 ALTER TABLE "store" ENABLE KEYS */;


-- Volcando datos para la tabla public.product: -1 rows
/*!40000 ALTER TABLE "product" DISABLE KEYS */;
INSERT INTO "product" ("id", "name", "description", "stock", "price", "image", "available", "store_id", "productLine_id") VALUES
	(1, 'Aguacate Hass', 'Kilogramo, Fruta de produccion libre de quimicos  con responsabilidad ambiental', 50, 8500, 'https://www.mercadoscampesinos.gov.co/wp-content/uploads/2021/04/aguacate-has.webp', 'true', 1, 1),
	(2, 'Borojo', 'Kilogramo,Fruta contiene principalmente fructosa y glucosa y cantidades importantes de proteínas, fósforo y vitamina B y C', 80, 7500, 'https://www.colombiamagica.co/imgs_articulos/borojo-colombia.jpg', 'true', 2, 1),
	(3, 'Zanahoria', 'Kilogramo, Fruta de produccion libre de quimicos  con responsabilidad ambiental', 100, 2800, 'https://elpoderdelconsumidor.org/wp-content/uploads/2021/05/zanahorias.png', 'true', 1, 2),
	(4, 'Apio', 'Mata, Producto hortaliza  producida  libre de quimicos, campesinos consientes que  usan insumos de origen natural', 80, 3600, 'https://encolombia.com/wp-content/uploads/2022/01/Cultivo-de-Apio-696x398.jpg', 'true', 1, 2),
	(5, 'Huevo Criollo', 'cubeta por 30 unidades, Huevos  criollos  gallinas de patio alimentadas  con maiz, caña, bore.', 100, 24000, 'https://www.mercadoscampesinos.gov.co/wp-content/uploads/2021/04/Huevos-criollos-1-400x400.jpg', 'true', 2, 3),
	(6, 'Queso campesino artesanal', 'Libra, Producto de tradición familiar echo a base de leche natural.', 90, 10300, 'https://i2.wp.com/elcondadodelascarnes.com/wp-content/uploads/2020/10/queso-campesino-scaled.jpg', 'true', 3, 3),
	(7, 'Plátano hartón verde', 'Kilogramo,Producto plátano  cultivo convencional', 200, 3200, 'https://www.mercadoscampesinos.gov.co/wp-content/uploads/2021/04/Platano-1-400x400.webp', 'true', 3, 4),
	(8, 'Auyama', 'Kilogramo, Kilogramo, Producto verdura  producida  libre de quimicos, campesinos consientes que  usan insumos de origen natural', 300, 3500, 'https://www.mercadoscampesinos.gov.co/wp-content/uploads/2021/04/Auyama-comun-400x400.jpg', 'true', 3, 9),
	(9, 'Arveja en cascara', 'Kilogramo, Arveja  verde  en vaina  es cultivado por agricultores que utilizan insumos de origen natura', 250, 8600, 'https://www.mercadoscampesinos.gov.co/wp-content/uploads/2021/04/Arveja-en-vaina-400x400.jpg', 'true', 2, 8);
/*!40000 ALTER TABLE "product" ENABLE KEYS */;


/*!40000 ALTER TABLE "product_line" ENABLE KEYS */;

-- Volcando datos para la tabla public.store: -1 rows
/*!40000 ALTER TABLE "store" DISABLE KEYS */;


/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
