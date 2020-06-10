from pandas import DataFrame
def sih(df,data):
    errorMessage=None
    try:
        if data[0] in list(df.describe().columns):
            data[2] = float(data[2])

        if data[3] == 'Null':
            if data[1] == '>':
                temp = df[df[data[0]] > data[2]]
                return temp
            elif data[1] == '<':
                temp = df[df[data[0]] < data[2]]
                return temp
            elif data[1] == '=':
                temp = df[df[data[0]] == data[2]]
                return temp

            else:
                temp = df[df[data[0]] != data[2]]
                return temp
        else:
            if data[0] in list(df.describe().columns):
                data[5] = float(data[5])

            '''
            各种情况对应的操作
            '''
            if data[3] == 'and':
                if data[1] == '>' and data[4] == '>':
                    temp = df[(df[data[0]] > data[2]) & (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '>' and data[4] == '<':
                    temp = df[(df[data[0]] > data[2]) & (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '>' and data[4] == '≠':
                    temp = df[(df[data[0]] > data[2]) & (df[data[0]] != data[5])]
                    return temp
                elif data[1] == '>' and data[4] == '=':
                    temp = df[(df[data[0]] > data[2]) & (df[data[0]] == data[5])]
                    return temp




                elif data[1] == '<' and data[4] == '>':
                    temp = df[(df[data[0]] < data[2]) & (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '<' and data[4] == '<':
                    temp = df[(df[data[0]] < data[2]) & (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '<' and data[4] == '≠':
                    temp = df[(df[data[0]] < data[2]) & (df[data[0]] != data[5])]
                    return temp
                elif data[1] == '<' and data[4] == '=':
                    temp = df[(df[data[0]] < data[2]) & (df[data[0]] == data[5])]
                    return temp



                elif data[1] == '≠' and data[4] == '>':
                    temp = df[(df[data[0]] != data[2]) & (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '≠' and data[4] == '<':
                    temp = df[(df[data[0]] != data[2]) & (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '≠' and data[4] == '=':
                    temp = df[(df[data[0]] != data[2]) & (df[data[0]] == data[5])]
                    return temp
                elif data[1] == '≠' and data[4] == '≠':
                    temp = df[(df[data[0]] != data[2]) & (df[data[0]] != data[5])]
                    return temp



                elif data[1] == '=' and data[4] == '=':
                    temp = df[(df[data[0]] == data[2]) & (df[data[0]] == data[5])]
                    return temp
                elif data[1] == '=' and data[4] == '>':
                    temp = DataFrame()
                    return temp
                elif data[1] == '=' and data[4] == '<':
                    temp =DataFrame()
                    return temp
                elif data[1] == '=' and data[4] == '≠':
                    temp =DataFrame()
                    return temp



            elif data[3] == 'or':
                if data[1] == '>' and data[4] == '>':
                    temp = df[(df[data[0]] > data[2]) | (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '>' and data[4] == '<':
                    temp = df[(df[data[0]] > data[2]) | (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '>' and data[4] == '≠':
                    temp = df[(df[data[0]] > data[2]) | (df[data[0]] != data[5])]
                    return temp
                elif data[1] == '>' and data[4] == '=':
                    temp = df[(df[data[0]] > data[2]) | (df[data[0]] == data[5])]
                    return temp




                elif data[1] == '<' and data[4] == '>':
                    temp = df[(df[data[0]] < data[2]) | (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '<' and data[4] == '<':
                    temp = df[(df[data[0]] < data[2]) | (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '<' and data[4] == '≠':
                    temp = df[(df[data[0]] < data[2]) | (df[data[0]] != data[5])]
                    return temp
                elif data[1] == '<' and data[4] == '=':
                    temp = df[(df[data[0]] < data[2]) | (df[data[0]] == data[5])]
                    return temp



                elif data[1] == '≠' and data[4] == '>':
                    temp = df[(df[data[0]] != data[2]) | (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '≠' and data[4] == '<':
                    temp = df[(df[data[0]] != data[2]) | (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '≠' and data[4] == '≠':
                    temp = df[(df[data[0]] != data[2]) | (df[data[0]] != data[5])]
                    return temp
                elif data[1] == '≠' and data[4] == '=':
                    temp = df[(df[data[0]] != data[2]) | (df[data[0]] == data[5])]
                    return temp



                elif data[1] == '=' and data[4] == '=':
                    temp = df[(df[data[0]] == data[2]) | (df[data[0]] == data[5])]
                    return temp
                elif data[1] == '=' and data[4] == '>':
                    temp = df[(df[data[0]] == data[2]) | (df[data[0]] > data[5])]
                    return temp
                elif data[1] == '=' and data[4] == '<':
                    temp = df[(df[data[0]] == data[2]) | (df[data[0]] < data[5])]
                    return temp
                elif data[1] == '=' and data[4] == '≠':
                    temp = df[(df[data[0]] == data[2]) | (df[data[0]] != data[5])]
                    return temp

    except Exception as e:
        errorMessage=str(e.args)
    finally:
        if errorMessage is not None:
         return errorMessage










