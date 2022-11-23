'''

여러개의 json file을 입력으로 받아 하나의 file로 merge 시켜주는 코드

'''
import os
import json
from natsort import natsorted

def main():
    # 경로받아오고 file list 생성
    file_path = "../split_output"
    file_list = natsorted(os.listdir(file_path))

    # base json file 선언
    base_in_file_path = file_path + "/" + file_list[0]
    with open(base_in_file_path, 'r') as base_input_json_file:
        base_json_file = json.load(base_input_json_file)
        base_json_file["images"].pop()
        base_json_file["annotations"].pop()

    # 모든 json file의 정보를 base json file에 insert
    for i in range(len(file_list)):
        in_file_path = file_path + "/" + file_list[i]
        with open(in_file_path, 'r') as input_json_file:
            json_file = json.load(input_json_file)

            # id 순서대로 변경
            json_file["images"][0]["id"] = i+1
            json_file["annotations"][0]["id"] = i+1
            json_file["annotations"][0]["image_id"] = i+1

            # for j in range(len(json_file["images"])):
            for j in range(1):
                # base_json_file["images"].insert(j,json_file["images"][j])
                # base_json_file["annotations"].insert(j,json_file["annotations"][j])
                base_json_file["images"].append(json_file["images"][j])
                base_json_file["annotations"].append(json_file["annotations"][j])

    # 변경된 사항 저장
    with open(f"../merge_output/merge.json","w", encoding= 'utf-8') as write_file:
        json.dump(base_json_file, write_file, indent="\t")
    
    return


if __name__ == "__main__":
    main()
