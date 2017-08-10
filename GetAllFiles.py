import time, json, csv,io

if __name__ == '__main__':
    datas = []
    with open('./AVS.txt') as data_file:
        datas = json.load(data_file)
    del datas[len(datas)-1]
    for d in datas:
        d['rename']=d['name'].split(' ')[0].split('.')[0].upper()
    print('total '+str(len(datas)))
    with open('./List.txt','w',encoding='utf-8') as outfile:
        data = json.dumps(datas, sort_keys = True, indent = 4, ensure_ascii=False)
        outfile.write(data)
        outfile.close()
