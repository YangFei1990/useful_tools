import os

from typing import List, Dict


def extract_results_from_log(log_abspath: str) -> Dict[str, float]:
    """
    Returns results as floats. Results returned (duration is secs):
    [
        'bbox-0.5'
        'bbox-0.5:0.95'
        'bbox-0.75'
        'bbox-small'
        'bbox-medium'
        'bbox-large'
        'segm-0.5'
        'segm-0.5:0.95'
        'segm-0.75'
        'segm-small'
        'segm-medium'
        'segm-large'
        'duration'
    ]
    """

    result_lines = {}



    with open(log_abspath, 'r') as log:
        for line in log:
            if 'Total duration' in line:
                result_lines['duration'] = line

            elif "mAP(bbox)/IoU=0.5: " in line:
                result_lines['bbox-0.5'] = line

            elif "mAP(bbox)/IoU=0.5:0.95: " in line:
                result_lines['bbox-0.5:0.95'] = line

            elif "mAP(bbox)/IoU=0.75: " in line:
                result_lines['bbox-0.75'] = line

            elif "mAP(bbox)/large: " in line:
                result_lines['bbox-large'] = line

            elif "mAP(bbox)/medium: " in line:
                result_lines['bbox-medium'] = line

            elif "mAP(bbox)/small: " in line:
                result_lines['bbox-small'] = line

            elif "mAP(segm)/IoU=0.5: " in line:
                result_lines['segm-0.5'] = line

            elif "mAP(segm)/IoU=0.5:0.95: " in line:
                result_lines['segm-0.5:0.95'] = line

            elif "mAP(segm)/IoU=0.75: " in line:
                result_lines['segm-0.75'] = line

            elif "mAP(segm)/large: " in line:
                result_lines['segm-large'] = line

            elif "mAP(segm)/medium: " in line:
                result_lines['segm-medium'] = line

            elif "mAP(segm)/small: " in line:
                result_lines['segm-small'] = line

            else:
                continue

    # Extract result from end fof line as a string
    def result(result_line):
        return float(result_line.split(": ")[1].strip().replace(",", ""))


    return {
        "bbox-0.5":      result(result_lines['bbox-0.5']),
        "bbox-0.5:0.95": result(result_lines['bbox-0.5:0.95']),
        'bbox-0.75':     result(result_lines['bbox-0.75']),
        'bbox-small':    result(result_lines['bbox-small']),
        'bbox-medium':   result(result_lines['bbox-medium']),
        'bbox-large':    result(result_lines['bbox-large']),

        'segm-0.5':      result(result_lines['segm-0.5']),
        'segm-0.5:0.95': result(result_lines['segm-0.5:0.95']),
        'segm-0.75':     result(result_lines['segm-0.75']),
        'segm-small':    result(result_lines['segm-small']),
        'segm-medium':   result(result_lines['segm-medium']),
        'segm-large':    result(result_lines['segm-large']),

        'duration':      result(result_lines['duration'])
    }



def order_results(parsed_results: Dict[str, float]) -> List[float]:
    return [
        parsed_results['bbox-0.5'],
        parsed_results['bbox-0.5:0.95'],
        parsed_results['bbox-0.75'],
        parsed_results['bbox-large'],
        parsed_results['bbox-medium'],
        parsed_results['bbox-small'],

        parsed_results['segm-0.5'],
        parsed_results['segm-0.5:0.95'],
        parsed_results['segm-0.75'],
        parsed_results['segm-large'],
        parsed_results['segm-medium'],
        parsed_results['segm-small'],

        parsed_results['duration']
    ]


if __name__ == '__main__':
    # BASE_PATH = "/Users/armanmcq/documents/maskrcnn-results/fixes_24epochkuybv  "
    # node_ids = list(range(1, 31))
    #
    # for node_id in node_ids:
    #     log_path = f'{BASE_PATH}/{node_id}.log'
    #     print(log_path)

    #BASE_PATH = f'/Users/fewu/Documents/maskRCNN_logs/seed1234_8x8_nopredefinedpadding'
    BASE_PATH = f'/Users/fewu/Documents/maskRCNN_logs/new_results/freeze_backbone'
    all_csv_lines = []
    #for gpu_count in ["8x1", "8x2", "8x4"]:
        #for padding in ["nopadding","padding"]:
            #for run_id in range(5):
    #for i in range(5,15):
    cnt = 1
    for i in range(5):
        #log_path = f'{BASE_PATH}/seed1234_8x8_nopredefinedpadding_{i}.log'
        log_path = f'{BASE_PATH}/32x4_freeze_{i}.log'
        if not os.path.isfile(log_path):
            # okay if missing?
            # assert os.path.isfile(log_path), f'Log file missing at {log_path}'
            continue


                #prefix = [f'{gpu_count}', f'{padding}', f'run{run_id}']
        #prefix = [f'seed1234_8x8_nopredefinedpadding_{i}']
        prefix = [f'32x4_freeze_{i}']
        cnt += 1
        results = [str(r) for r in order_results(extract_results_from_log(log_path))]


        all_csv_lines.append(prefix + results)

    for csv_line in all_csv_lines:
        print(",".join(csv_line))

    with open(f'{BASE_PATH}/combined_32x4_freeze.csv', 'w+') as f:
        for csv_line in all_csv_lines:
            f.write(",".join(csv_line) + "\n")
