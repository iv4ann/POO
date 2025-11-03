-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 08-10-2025 a las 16:41:19
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_coches`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autos`
--

CREATE TABLE `autos` (
  `id` int(11) NOT NULL,
  `marca` varchar(60) NOT NULL,
  `color` varchar(60) NOT NULL,
  `modelo` varchar(4) NOT NULL,
  `velocidad` int(11) NOT NULL,
  `caballaje` int(11) NOT NULL,
  `plazas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `autos`
--

INSERT INTO `autos` (`id`, `marca`, `color`, `modelo`, `velocidad`, `caballaje`, `plazas`) VALUES
(1, 'VW', 'AMARILLO', '2020', 200, 180, 5),
(2, 'VOLVO', 'ROJO', '2025', 180, 170, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camiones`
--

CREATE TABLE `camiones` (
  `id` int(11) NOT NULL,
  `marca` varchar(60) NOT NULL,
  `color` varchar(60) NOT NULL,
  `modelo` varchar(4) NOT NULL,
  `velocidad` int(11) NOT NULL,
  `caballaje` int(11) NOT NULL,
  `plazas` int(11) NOT NULL,
  `eje` int(11) NOT NULL,
  `capacidadcarga` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `camiones`
--

INSERT INTO `camiones` (`id`, `marca`, `color`, `modelo`, `velocidad`, `caballaje`, `plazas`, `eje`, `capacidadcarga`) VALUES
(2, 'W', 'E', 'R', 4, 5, 2, 2, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `camionetas`
--

CREATE TABLE `camionetas` (
  `id` int(11) NOT NULL,
  `marca` varchar(60) NOT NULL,
  `color` varchar(60) NOT NULL,
  `modelo` varchar(4) NOT NULL,
  `velocidad` int(11) NOT NULL,
  `caballaje` int(11) NOT NULL,
  `plazas` int(11) NOT NULL,
  `traccion` varchar(60) NOT NULL,
  `cerrada` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autos`
--
ALTER TABLE `autos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `camiones`
--
ALTER TABLE `camiones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `camionetas`
--
ALTER TABLE `camionetas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `autos`
--
ALTER TABLE `autos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `camiones`
--
ALTER TABLE `camiones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `camionetas`
--
ALTER TABLE `camionetas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
