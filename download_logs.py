import subprocess
'''
ips = ["ec2-3-80-161-68.compute-1.amazonaws.com",
"ec2-18-206-182-75.compute-1.amazonaws.com",
"ec2-34-235-161-99.compute-1.amazonaws.com",
"ec2-3-216-28-54.compute-1.amazonaws.com",
"ec2-100-24-65-65.compute-1.amazonaws.com",
"ec2-34-205-54-230.compute-1.amazonaws.com",
"ec2-54-162-49-115.compute-1.amazonaws.com",
"ec2-34-235-163-58.compute-1.amazonaws.com",
"ec2-54-237-155-231.compute-1.amazonaws.com",
"ec2-34-229-21-193.compute-1.amazonaws.com",
"ec2-54-174-182-58.compute-1.amazonaws.com",
"ec2-35-170-59-35.compute-1.amazonaws.com",
"ec2-18-209-231-28.compute-1.amazonaws.com",
"ec2-100-27-15-149.compute-1.amazonaws.com",
"ec2-100-24-124-131.compute-1.amazonaws.com",
"ec2-54-81-7-111.compute-1.amazonaws.com",
"ec2-3-82-43-61.compute-1.amazonaws.com",
"ec2-34-201-137-84.compute-1.amazonaws.com",
"ec2-54-84-122-115.compute-1.amazonaws.com",
"ec2-54-225-38-117.compute-1.amazonaws.com",
"ec2-34-200-215-201.compute-1.amazonaws.com",
"ec2-34-201-21-91.compute-1.amazonaws.com",
"ec2-34-237-136-197.compute-1.amazonaws.com",
"ec2-34-205-172-177.compute-1.amazonaws.com",
"ec2-54-225-56-209.compute-1.amazonaws.com",
"ec2-3-94-148-183.compute-1.amazonaws.com",
"ec2-3-216-80-176.compute-1.amazonaws.com",
"ec2-3-216-132-118.compute-1.amazonaws.com",
"ec2-3-94-29-173.compute-1.amazonaws.com",
"ec2-54-236-62-38.compute-1.amazonaws.com"]
'''
ips = ["ec2-100-26-245-164.compute-1.amazonaws.com",
        "ec2-100-26-5-159.compute-1.amazonaws.com",
        "ec2-100-25-248-14.compute-1.amazonaws.com"]

output_dir = "/Users/fewu/Documents/maskRCNN_logs"
conf = ["8x1", "8x2", "8x4", "8x1", "8x2", "8x4"]
padding = ["nopadding","padding"]


if __name__ == '__main__':
    # for each ip, download file
    for i, ip in enumerate(ips):
        #if i > 4 and i < 15:
            #cur_conf = conf[i // 5]
            #cur_pad = padding[i // 15]
            #subprocess.check_output(f'ssh -i ~/.ssh/fewu-us-east-1.pem ubuntu@{ip} "./backup log_backup/seed1234_8x8_predefinedpadding"', shell=True)
            #out_app = f'/seed1234_8x8_nopredefinedpadding_{i}.log'
        out_app = '/new_results/freeze_backbone/'
        cur_out = output_dir + out_app
        #assert not output_dir.endswith('/')
        #subprocess.check_call(f'rm -rf {cur_out}', shell=True)
        #subprocess.check_call(f'mkdir -p {cur_out}', shell=True)
        subprocess.check_output(f'scp -r -i ~/.ssh/fewu-us-east-1.pem ec2-user@{ip}:/home/ec2-user/32x4_freeze* {cur_out}32x4_freeze_{i}.log', shell=True)
