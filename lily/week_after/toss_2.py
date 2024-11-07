import sys

input_assets = eval(sys.stdin.readline())

checked_assets = [] # 중복 및 validation한 자산 모음
validated_assets = [] # 유효한 자산 모음

def validate_assets(re_year, asset_code, re_month, re_order):
    return validate_re_year(re_year) and validate_asset_code(asset_code) and validate_re_month(int(re_year), re_month) and validate_re_order(re_order)

def validate_re_year(re_year):
    return len(re_year) == 2 and 13 <= int(re_year) <= 22

def validate_asset_code(asset_code):
    return asset_code in ['SP', 'KE', 'MO', 'CO', 'DE']

def validate_re_month(re_year, re_month):
    if re_year == 13:
        return re_month in ['04', '05', '06', '07', '08', '09', '10', '11', '12']
    elif 14 <= re_year <= 21:
        return re_month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    else:
        return re_month in ['01', '02', '03', '04', '05', '06', '07', '08']

def validate_re_order(re_order):
    if len(re_order) == 2 and re_order.isdigit():
        re_order_int = int(re_order)
        return 1 <= re_order_int <= 99
    return False

for asset in input_assets:
    if asset in checked_assets:
        continue
    
    checked_assets.append(asset)

    ## validation
    if len(asset) != 9:
        continue

    parts = asset.split("-")
    if len(parts) != 2 or len(parts[1]) != 6:
        continue

    re_year = parts[0] # 등록 연도
    asset_code = parts[1][0:2] # 취급 자산 코드
    re_month = parts[1][2:4] # 등록 월
    re_order = parts[1][4:6] # 등록 순서

    if validate_assets(re_year, asset_code, re_month, re_order):
        validated_assets.append(asset)

asset_code_priority = {
    "SP": 1,
    "KE": 2,
    "MO": 3, 
    "CO": 4,
    "DE": 5
}

sorted_assets = sorted(validated_assets, key=lambda x: (int(x.split("-")[0]), asset_code_priority[x.split("-")[1][0:2]], int(x.split("-")[1][2:4]), int(x.split("-")[1][4:6])))

print(sorted_assets)
