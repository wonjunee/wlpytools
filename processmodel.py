import torch

def saving_models(models, Titlelist, save_data_path, epoch):
    for title in Titlelist:
        torch.save(models[title]['T'].state_dict(), f"{save_data_path}/{epoch}-{title}-T.pt")
        torch.save(models[title]['S'].state_dict(), f"{save_data_path}/{epoch}-{title}-S.pt")

def loading_models(models, Titlelist, save_data_path, epoch):
    for title in Titlelist:
        models[title]['T'].load_state_dict(torch.load(f"{save_data_path}/{epoch}-{title}-T.pt"))
        models[title]['S'].load_state_dict(torch.load(f"{save_data_path}/{epoch}-{title}-S.pt"))



def get_model(model):
    T = model['T']
    S = model['S']
    phi = model['phi']
    optT = model['optT']
    optS = model['optS']
    optphi = model['optphi']
    return T,S,phi,optT,optS,optphi
