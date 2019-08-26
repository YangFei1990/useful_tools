import os

def cal_step(file_name):
    file = file_name.split('x')
    return float(file[0]) * float(file[1][:-4])

log_path = '/Users/fewu/Documents/maskRCNN_logs/template(docker)/mask_rcnn'
files = os.listdir(log_path)
all_throughput = []
for file in files:
    if ".log" in file:
        throughput = []
        with open(log_path + '/' + file) as fp:
          line = fp.readline()
          while line:
              if "MeanEpochThroughput" in line:
                  throughput.append(float(line.split(' ')[-1]))
              line = fp.readline()
        max_throughput = max(throughput)
        mean_through = sum(throughput) / len(throughput)
        step_size = cal_step(file)
        avg_step_time = step_size / mean_through
        best_step_time = step_size / max_throughput
        print(f"{file}: max throughput {max_throughput}, average throughput {mean_through}, step size {step_size}, Avg step time {avg_step_time}, best step time {best_step_time}")

'''
param = [[],[],[],[]]
for line in log:
  print(f'Currently parsing: {line}')
  if "The mean is" in line:
      cur_log = line.split(",")
      for i in range(4):
          param[i].append(float(cur_log[i].split(' ')[-1]))
avg_mean = sum(param[0]) / len(param[0])
avg_slow = sum(param[1) / len(param[1])
avg_fast = sum(param[2]) / len(param[2])
print('Average mean is {}, average slowest flow is {}, average fastest flow is {}\n'.format(avg_mean, avg_slow, avg_fast))
avg_sdv = sum(param[3]) / len(param[3])
max_sdv = max(param[3])
min_sdv = min(param[3])
print('Average standard deviation is {}, highest standard deviation is {}, lowest standard deviation is {}\n'.format(avg_sdv, max_sdv, min_sdv))
'''
