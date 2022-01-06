def solution(triangle):
    dp = {}
    for layer, values in enumerate(triangle):
        if layer == 0:
            dp[layer] = values
        else:
            previous_layer = dp[layer-1]
            layer_vals = [-1 for _ in range(layer+1)]
            for idx, val in enumerate(previous_layer):
                layer_vals[idx] = max(layer_vals[idx], val + values[idx])
                layer_vals[idx+1] = max(layer_vals[idx+1], val + values[idx+1])
            dp[layer] = layer_vals
    answer = max(dp[len(triangle)-1])
    return answer