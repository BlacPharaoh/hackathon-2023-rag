import os

if __name__ == "__main__":
    from main import predict

    print(predict(data_source="k8", prompt="What is the control plane?"))
