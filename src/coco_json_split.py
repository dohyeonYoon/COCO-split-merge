'''

json file을 입력으로 받아 file_name별로 split 해주는 코드

'''
import json

def main():
    # 경로설정
    file_name = "test" #### 여기를 바꿔주세요 ###
    file_path = '../input/'
    in_file_path= file_path+ f'{file_name}.json'

    with open(in_file_path,'r') as input_json_file, open(in_file_path,'r') as input_json_file2:
        # json file을 읽기
        json_file = json.load(input_json_file)
        json_file2 = json.load(input_json_file2)

        for i in range(len(json_file["images"])):
            # json_file의 "images", "annotations" key에 해당하는 기존 value값 전체 빼기
            json_file["images"].pop()
            json_file["annotations"].pop()

        for j in range(len(json_file2["images"])):
            # 비어있는 "images", "annotations" key에 해당하는 value에 file_name별로 삽입
            base_json_file = json_file
            save_file_name = json_file2["images"][j]["file_name"][:-4]
            base_json_file["images"].insert(j,json_file2["images"][j])
            base_json_file["annotations"].insert(j,json_file2["annotations"][j])

            # 변경된 사항 저장
            with open(f"../split_output/{save_file_name}.json","w", encoding= 'utf-8') as write_file:
                json.dump(base_json_file, write_file, indent="\t")

            # insert된 값 빼서 dictionary 초기화
            base_json_file["images"].pop()
            base_json_file["annotations"].pop()
    return

if __name__ == "__main__":
    main()