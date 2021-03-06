-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema crm_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `crm_schema` ;

-- -----------------------------------------------------
-- Schema crm_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `crm_schema` DEFAULT CHARACTER SET utf8 ;
USE `crm_schema` ;

-- -----------------------------------------------------
-- Table `crm_schema`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crm_schema`.`users` ;

CREATE TABLE IF NOT EXISTS `crm_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `f_name` VARCHAR(45) NULL,
  `l_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` LONGTEXT NULL,
  `todos_fin` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `crm_schema`.`tasks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `crm_schema`.`tasks` ;

CREATE TABLE IF NOT EXISTS `crm_schema`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `task_description` LONGTEXT NULL,
  `priority` INT NULL,
  `is_recurring` INT NULL,
  `reminder_time` TIME NULL,
  `due_date` DATE NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `crm_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
