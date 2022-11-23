'''

json file을 입력으로 받아  file_name을 변경시켜주는 코드

'''

import json

def main():
    # 경로설정
    file_name = "004" #### 여기를 바꿔주세요 ###
    file_path = './annotation/'
    in_file_path= file_path+ f'{file_name}.json'

    with open(in_file_path,'r') as input_json_file:
        # json file을 읽기
        json_file = json.load(input_json_file)

        for i in range(len(json_file["images"])):
            # json_file의 "images", "annotations" key에 해당하는 기존 value값 전체 빼기
            json_file["images"][i]["file_name"] = "004_" + json_file["images"][i]["file_name"]

            # 변경된 사항 저장
            with open(f"./edit_output/{file_name}_v02.json","w", encoding= 'utf-8') as write_file:
                json.dump(json_file, write_file, indent="\t")

    return

if __name__ == "__main__":
    main()