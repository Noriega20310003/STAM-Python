-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 02-12-2019 a las 06:59:47
-- Versión del servidor: 5.7.27-log
-- Versión de PHP: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `juegos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `desarrollador`
--

CREATE TABLE `desarrollador` (
  `iddesarrollador` int(11) NOT NULL,
  `contra` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `nombredes` varchar(60) COLLATE utf8_spanish_ci NOT NULL,
  `iddist` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `desarrollador`
--

INSERT INTO `desarrollador` (`iddesarrollador`, `contra`, `nombredes`, `iddist`) VALUES
(12, '$2b$12$wTVVWJNIvYHxXWinwefco.Yp4Hgy9cx1GkYH6TnGuzmLRtqN1w/YW', '123@123', 3),
(13, '$2b$12$XdHzRm72wpS2fpBWYG7l8.SY/vzimzAVW84GGcnROmWbeyy1/zHYe', '123@123', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dist`
--

CREATE TABLE `dist` (
  `iddist` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fd` date NOT NULL,
  `clausulas` text COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `dist`
--

INSERT INTO `dist` (`iddist`, `nombre`, `fd`, `clausulas`) VALUES
(1, 'asda', '2019-12-04', 'asdas'),
(3, 'qweq', '2019-12-05', 'zxcz'),
(4, 'Stam Industries', '2017-08-16', 'Cod 20.950, modulo de distribucion 21 09 ');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `juego`
--

CREATE TABLE `juego` (
  `idg` int(11) NOT NULL,
  `version` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `DLC` int(11) NOT NULL,
  `nomreg` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `pg` int(11) NOT NULL,
  `genero` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fechadist` date NOT NULL,
  `compat` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `opgraficos` text COLLATE utf8_spanish_ci NOT NULL,
  `valoracion` float NOT NULL,
  `bloqueo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `pracio` float NOT NULL,
  `dn` int(11) NOT NULL,
  `iddist` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `juego`
--

INSERT INTO `juego` (`idg`, `version`, `DLC`, `nomreg`, `pg`, `genero`, `fechadist`, `compat`, `opgraficos`, `valoracion`, `bloqueo`, `pracio`, `dn`, `iddist`) VALUES
(1, '1', 1, '1', 1, '1', '0001-01-01', '1', '1', 1, 'Mexico', 1, 1, 1),
(3, '20.5.00960', 3, 'Street Of Rage 15', 16, 'pelea', '2063-05-05', 'Windous H32', 'GTX 3080 TiX / i9x 18667k', 9, 'Mexico', 650, 12, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servidor`
--

CREATE TABLE `servidor` (
  `ids` int(11) NOT NULL,
  `ips` int(50) NOT NULL,
  `tipo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `rack` int(11) NOT NULL,
  `puerto` int(20) NOT NULL,
  `cusuario` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `ms` int(11) NOT NULL,
  `idg` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `terminoslegales`
--

CREATE TABLE `terminoslegales` (
  `idterm` int(11) NOT NULL,
  `articulos` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `region` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `nombreterm` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `fechaterm` date NOT NULL,
  `nserie` int(80) NOT NULL,
  `idg` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `transaccion`
--

CREATE TABLE `transaccion` (
  `idt` int(11) NOT NULL,
  `NT` int(11) NOT NULL,
  `metodo` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `verificacion` int(80) NOT NULL,
  `idu` int(11) NOT NULL,
  `idg` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `transaccion`
--

INSERT INTO `transaccion` (`idt`, `NT`, `metodo`, `verificacion`, `idu`, `idg`) VALUES
(3, 123, 'efectivo', 123, 2, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `idu` int(11) NOT NULL,
  `region` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `direccionfactura` text COLLATE utf8_spanish_ci NOT NULL,
  `nombreusuario` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `tarjeta` int(30) NOT NULL,
  `contra` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`idu`, `region`, `direccionfactura`, `nombreusuario`, `tarjeta`, `contra`) VALUES
(2, 'Mexico', 'paseo de las galateas 1152', 'Kalmons', 285221, '$2b$12$cWw1lkjICYzuf30rJPX8A.3xXfXWEOLMErlLNRFAn33GBczwCGjNu');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `desarrollador`
--
ALTER TABLE `desarrollador`
  ADD PRIMARY KEY (`iddesarrollador`),
  ADD KEY `idd` (`iddist`) USING BTREE;

--
-- Indices de la tabla `dist`
--
ALTER TABLE `dist`
  ADD PRIMARY KEY (`iddist`);

--
-- Indices de la tabla `juego`
--
ALTER TABLE `juego`
  ADD PRIMARY KEY (`idg`),
  ADD KEY `idd` (`iddist`);

--
-- Indices de la tabla `servidor`
--
ALTER TABLE `servidor`
  ADD PRIMARY KEY (`ids`),
  ADD KEY `idg` (`idg`);

--
-- Indices de la tabla `terminoslegales`
--
ALTER TABLE `terminoslegales`
  ADD PRIMARY KEY (`idterm`),
  ADD KEY `idg` (`idg`);

--
-- Indices de la tabla `transaccion`
--
ALTER TABLE `transaccion`
  ADD PRIMARY KEY (`idt`),
  ADD KEY `idg` (`idg`),
  ADD KEY `idu` (`idu`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`idu`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `desarrollador`
--
ALTER TABLE `desarrollador`
  MODIFY `iddesarrollador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `dist`
--
ALTER TABLE `dist`
  MODIFY `iddist` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `juego`
--
ALTER TABLE `juego`
  MODIFY `idg` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `servidor`
--
ALTER TABLE `servidor`
  MODIFY `ids` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `terminoslegales`
--
ALTER TABLE `terminoslegales`
  MODIFY `idterm` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `transaccion`
--
ALTER TABLE `transaccion`
  MODIFY `idt` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `idu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `desarrollador`
--
ALTER TABLE `desarrollador`
  ADD CONSTRAINT `iddist2` FOREIGN KEY (`iddist`) REFERENCES `dist` (`iddist`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `juego`
--
ALTER TABLE `juego`
  ADD CONSTRAINT `iddist` FOREIGN KEY (`iddist`) REFERENCES `dist` (`iddist`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `servidor`
--
ALTER TABLE `servidor`
  ADD CONSTRAINT `fidg` FOREIGN KEY (`idg`) REFERENCES `juego` (`idg`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `terminoslegales`
--
ALTER TABLE `terminoslegales`
  ADD CONSTRAINT `terminoslegales_ibfk_1` FOREIGN KEY (`idg`) REFERENCES `juego` (`idg`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `transaccion`
--
ALTER TABLE `transaccion`
  ADD CONSTRAINT `idg` FOREIGN KEY (`idg`) REFERENCES `juego` (`idg`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `idu` FOREIGN KEY (`idu`) REFERENCES `usuario` (`idu`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
