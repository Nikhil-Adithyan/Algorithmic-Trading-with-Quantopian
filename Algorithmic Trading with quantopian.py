# Initializing and Scheduling 

def initialize(context):
    context.facebook = sid(42950)
    context.amazon = sid(16841)
    context.apple = sid(24)
    context.netflix = sid(23709)
    context.google = sid(26578)
    schedule_function(ma_strategy, date_rules.every_day(), time_rules.market_open(hours = 1))

# Creating strategy

def ma_strategy(context, data):
    # a. Getting historical data on stock prices
    hist_facebook = data.history(context.facebook, 'price',50, '1d')
    hist_amazon = data.history(context.amazon, 'price',50, '1d')
    hist_apple = data.history(context.apple, 'price',50, '1d')
    hist_netflix = data.history(context.netflix, 'price',50, '1d')
    hist_google = data.history(context.google, 'price',50, '1d')
    # b. setting log info
    log.info(hist_facebook.head())
    log.info(hist_amazon.head())
    log.info(hist_apple.head())
    log.info(hist_netflix.head())
    log.info(hist_google.head())
    # c. creating SMA indicators 
    sma20_facebook = hist_facebook[-20:].mean()
    sma20_amazon = hist_amazon[-20:].mean()
    sma20_apple = hist_apple[-20:].mean()
    sma20_netflix = hist_netflix[-20:].mean()
    sma20_google = hist_google[-20:].mean()
    sma50_facebook = hist_facebook[-50:].mean()
    sma50_amazon = hist_amazon[-50:].mean()
    sma50_apple = hist_apple[-50:].mean()
    sma50_netflix = hist_netflix[-50:].mean()
    sma50_google = hist_google[-50:].mean()
    
    open_orders = get_open_orders()
    
    # d. Creating trading strategy for Buy
    if sma20_facebook > sma50_facebook:
        if context.facebook not in open_orders:
            order_target_percent(context.facebook, 0.20)
    if sma20_amazon > sma50_amazon:
        if context.amazon not in open_orders:
            order_target_percent(context.amazon, 0.20)
    if sma20_apple > sma50_apple:
        if context.apple not in open_orders:
            order_target_percent(context.apple, 0.20)
    if sma20_netflix > sma50_netflix:
        if context.netflix not in open_orders:
            order_target_percent(context.netflix, 0.20)
    if sma20_google > sma50_google:
        if context.google not in open_orders:
            order_target_percent(context.google, 0.20)
    # Creating trading strategy for Sell 
    elif sma50_facebook > sma20_facebook:
        if context.facebook not in open_orders:
            order_target_percent(context.facebook, -0.20)
    elif sma50_amazon > sma20_amazon:
        if context.amazon not in open_orders:
            order_target_percent(context.amazon, -0.20)
    elif sma50_apple > sma20_apple:
        if context.apple not in open_orders:
            order_target_percent(context.apple, -0.20)
    elif sma50_netflix > sma20_netflix:
        if context.netflix not in open_orders:
            order_target_percent(context.netflix, -0.20)
    elif sma50_google > sma20_google:
        if context.google not in open_orders:
            order_target_percent(context.google, -0.20)
    # Custom variable for leveraging liquidity
    record(leverage = context.account.leverage)