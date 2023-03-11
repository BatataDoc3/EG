def gen_html(alunos, biggest_notas):
    html = '''
    <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8"/>
                <title>Notas</title>
            </head>
            <body>
            '''
    for i, turma in enumerate(alunos):
        html += f'''
                <h2>Turma {i}</h2>
                <table>
                    <tr>
                    <th> Aluno </th>
                    '''
        for a in range(0, biggest_notas):
            html += f'<th> Nota {a} </th>'
        html += '</tr>'
        for aluno in turma:
            notas = aluno[1:]
            html += f'''
                    <tr>
                      <td>{aluno[0]}</td> '''
            for nota in notas:
                html += f'<td>{nota}</td>'

            html += '</tr>'
        
        html += '</table>' 

    html += '''
            </body>
        </html>
    '''
    f = open("pagHTML.html", "w")
    f.write(html)