#!/usr/bin/env python3
import sys
import os
import configparser
import subprocess
import logging
from datetime import datetime
from pathlib import Path

def setup_logging(log_dir):
    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d')
    log_file = log_path / f'orchestrator-{timestamp}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger(__name__)

def load_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    return config

def get_github_token(config):
    token_env = config.get('GLOBAL', 'github_token_env', fallback='GH_TOKEN')
    token = os.environ.get(token_env)
    if not token:
        raise ValueError(f'Variable de entorno {token_env} no definida')
    return token

def main():
    # Ruta base del orquestador (Squad Governance)
    base_path = Path(__file__).parent.parent
    config_file = base_path / 'config' / 'squads.ini'
    
    if not config_file.exists():
        print(f'ERROR: No se encuentra {config_file}')
        sys.exit(1)
    
    config = load_config(config_file)
    log_dir = base_path / config.get('GLOBAL', 'log_dir', fallback='logs')
    logger = setup_logging(log_dir)
    
    logger.info('='*60)
    logger.info('ORQUESTADOR MULTI-SQUAD - Squad Governance')
    logger.info('='*60)
    logger.info(f'Configuracion: {config_file}')
    
    try:
        token = get_github_token(config)
        logger.info(f'Token GitHub cargado correctamente')
    except ValueError as e:
        logger.error(str(e))
        sys.exit(1)
    
    # Procesar cada squad
    squads = [s for s in config.sections() if s != 'GLOBAL']
    logger.info(f'Squads configurados: {len(squads)}')
    
    total_repos = 0
    for squad_section in squads:
        squad_name = config.get(squad_section, 'name', fallback=squad_section)
        repositories = config.get(squad_section, 'repositories', fallback='').split(',')
        repositories = [r.strip() for r in repositories if r.strip()]
        total_repos += len(repositories)
        
        logger.info(f'  - {squad_name}: {len(repositories)} repositorios')
    
    logger.info(f'Total: {total_repos} repositorios en {len(squads)} squads')
    logger.info('')
    
    # Aqui se implementaria la logica de ejecucion de jobs
    # Por ahora solo mostramos la configuracion
    
    logger.info('='*60)
    logger.info('ORQUESTADOR - Configuracion validada correctamente')
    logger.info('='*60)

if __name__ == '__main__':
    main()
