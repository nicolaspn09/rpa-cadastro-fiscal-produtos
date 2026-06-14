from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Definir argumentos padrão da DAG
default_args = {
    'owner': 'seu_nome',  # Nome do responsável
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Criar a DAG
with DAG(
    dag_id='executar_cadastro_produto_fiscal',
    default_args=default_args,
    description='Executa o script de cadastro de produtos fiscais',
    schedule_interval='@hourly',  # Executar a cada uma hora
    start_date=datetime(2025, 1, 16),
    catchup=False,  # Não executar tarefas anteriores à data inicial
) as dag:

    # Tarefa para executar o script
    executar_script = BashOperator(
        task_id='rodar_cadastro_produtos_fiscal',
        bash_command=r'"Z:\Python\Cadastro Produto Fiscal (Senior)\main.pyw"',
    )

    # Define as dependências entre as tarefas (se houver mais de uma tarefa)
    executar_script
