import configparser
import logging
import os

from pydw.utils import connection

base_dir = os.path.dirname(__file__)
file_dir = base_dir + os.path.sep + 'dbconfig.ini'
cfg = configparser.ConfigParser()
cfg.read(file_dir)


def set_config(section, conf):
    if cfg.has_section(section):
        logging.error("The " + section + ' is already exists, please use update_config.')
        return False
    else:
        cfg_file = open(file_dir, 'w')
        cfg.add_section(section)
        cfg.set(section, 'type', conf.type)
        cfg.set(section, 'host', conf.host)
        cfg.set(section, 'port', conf.port)
        cfg.set(section, 'username', conf.username)
        cfg.set(section, 'password', conf.password)
        cfg.set(section, 'database', conf.database)
        cfg.set(section, 'encoding', conf.encoding)
        cfg.write(cfg_file)
        cfg_file.close()
        return True


def update_config(section, conf):
    if cfg.has_section(section):
        cfg_file = open(file_dir, 'w')
        cfg.remove_section(section)
        cfg.add_section(section)
        cfg.set(section, 'type', conf.type)
        cfg.set(section, 'host', conf.host)
        cfg.set(section, 'port', conf.port)
        cfg.set(section, 'username', conf.username)
        cfg.set(section, 'password', conf.password)
        cfg.set(section, 'database', conf.database)
        cfg.set(section, 'encoding', conf.encoding)
        cfg.write(cfg_file)
        cfg_file.close()
        return True
    else:
        logging.warning("The " + section + ' is not exists, please use set_config.')
        return False


def get_config(db_conn):
    if cfg.has_section(db_conn):
        conf = connection.Config(
            type=cfg.get(db_conn, 'type'),
            host=cfg.get(db_conn, 'host'),
            port=cfg.get(db_conn, 'port'),
            username=cfg.get(db_conn, 'username'),
            password=cfg.get(db_conn, 'password'),
            database=cfg.get(db_conn, 'database'),
            encoding=cfg.get(db_conn, 'encoding')
        )
        return conf
    else:
        logging.error('[' + db_conn + '] is not in ' + base_dir + os.path.sep + 'dbconfig.ini.')
        return -1


def remove_config(section):
    if cfg.has_section(section):
        logging.warning("The section [" + section + '] will be deleted.')
        cfg_file = open(file_dir, 'w')
        cfg.remove_section(section)
        cfg.write(cfg_file)
        cfg_file.close()
        return True
    else:
        logging.warning("The section [" + section + '] is not exists.')
        return False
