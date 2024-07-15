import pandas as pd
import csv
import sqlite3
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

def sql_to_csv():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('all_fault_line.db')
    
    # Obter cursor
    cursor = conn.cursor()
    
    # Executar consulta para obter todos os dados da tabela especificada
    cursor.execute("SELECT * FROM fault_lines")
    
    # Buscar todas as linhas
    rows = cursor.fetchall()
    
    # Obter nomes das colunas
    headers = [description[0] for description in cursor.description]

    # Preparar dados para o CSV
    csv_data = ','.join(headers) + '\n'  # Linha de cabeçalho
    for row in rows:
        csv_data += ','.join(map(str, row)) + '\n'

    # Criar uma caixa de diálogo para selecionar o arquivo de saída
    root = Tk()
    root.withdraw()  # Ocultar a janela principal do Tkinter
    file_path = asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])

    # Escrever os dados no arquivo CSV
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as csv_file:
            csv_file.write(csv_data)

    # Fechar a conexão
    conn.close()

# Parte II: Converter CSV para SQL
def csv_to_sql():
    # Esta linha cria o arquivo do banco de dados se ele não existir
    conn = sqlite3.connect('list_volcano.db')

    # Esta linha abre o CSV usando pandas
    df = pd.read_csv('list_volcano.csv')

    # Esta linha converte o CSV para banco de dados (db)
    df.to_sql('Volcanos', conn, if_exists='replace', index=False)

    # Criar um objeto cursor para manipular os dados
    cur = conn.cursor()

    # Buscar e exibir dados para fins de teste
    for row in cur.execute('SELECT * FROM Volcanos'):
        print(row)
        
    # Fechar a conexão
    conn.close()

# Chamar a função para exportar os dados do banco de dados para CSV
sql_to_csv()

# Chamar a função para importar os dados do CSV para o banco de dados
csv_to_sql()
