#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Last Modification : 2020.02.12.
"""
import time
import random
import os


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �������� ���� ������ �����մϴ�.
NUM_SAMPLES = 1000

# �̸��� ������ ����� ���� ���ڵ��� �����մϴ�.
alphabet_samples = "abcdefghizklmnopqrstuvwxyz1234567890"


# �������� ���õ� ���� ���ڸ� �����ϴ� �Լ��Դϴ�.
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result


# �̸� ������ ����� ���� ���ڵ��� �����մϴ�.
first_name_samples = "���̹���������������"
middle_name_samples = "�μ�������������ä����"
last_name_samples = "�������ȣ�ļ���������"


# �������� ��� �̸��� �����ϴ� �Լ��Դϴ�.
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


# ������� ������ ������ �����մϴ�.
os.mkdir("personal_info")

# �������� ������ �ڵ����� �����ϴ� �κ��Դϴ�.
# NUM_SAMPLES ȸ����ŭ �ݺ��մϴ�.
# �̸��׸�, NUM_SAMPLES�� 100�̸� ������ �������� ������ 100ȸ �ݺ��մϴ�.
for i in range(NUM_SAMPLES):
    # �������� ��� �̸��� �����մϴ�.
    name = random_name()

    # ����� ������ �̸��� �����մϴ�.
    filename = "personal_info/" + str(i) + "_" + name + ".txt"

    # ����� ������ �����մϴ�. �� �� ������ �����˴ϴ�.
    outfile = open(filename, 'w')

    # ����� ���Ͽ� �̸��� �����մϴ�.
    outfile.write("name : " + name + "\n")

    # ����� ���Ͽ� �������� ������ ���̸� �����մϴ�.
    outfile.write("age : " + str(time.time())[-2:] + "\n")

    # ����� ���Ͽ� �������� ������ �̸����� �����մϴ�.
    outfile.write("e-mail : " + random_string(8) + "@bhban.com\n")

    # ����� ���Ͽ� �������� ������ �μ����� �����մϴ�.
    outfile.write("division : " + random_string(3) + "\n")

    # ����� ���Ͽ� �������� ������ �ڵ��� ��ȣ�� �����մϴ�.
    outfile.write("telephone : 010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2] + '\n')

    # ����� ���Ͽ� �������� ������ ������ �����մϴ�.
    outfile.write("sex : " + random.choice(["male", "female"]))

    # ����� ���� ������ �������մϴ�.
    outfile.close()



# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
