import streamlit as st
import os
st.set_page_config(
    page_title="Coastal Hazard Transfer Functions  Project", page_icon=" 🌊",layout="wide" )


## https://tsunamitransferfunctionstest.streamlit.app/

st.title("Hazard Curves Model's Results")


description={'MLP_with_anchor_input': 'Multilayer perceptron with an onshore hazard curve as input',
             'MLP_without_anchor_input': 'Multilayer perceptron',
             'VAE_with_anchor_input': 'Variational Autoencoder with an onshore hazard curve as input',
             'VAE_without_anchor_input': 'Variational Autoencoder',
             'Enc_with_anchor_input': 'Neural Network Operator with an onshore hazard curve as input',
             'Enc_without_anchor_input': 'Neural Network Operator'
             }

# path to the experiments
path = os.path.abspath(os.path.dirname(__file__))
folds = [name for name in os.listdir(path) if os.path.isdir(name)]
experiments = [n for n in folds if '_input' in n]

pth2exp=dict()
for i in range(len(experiments)):
    # path to each experiment
    pth = os.path.join(path,experiments[i])
    # dictionary experiment = cases
    pth2exp[experiments[i]] = pth

def floss(ruta):
    archivos = os.listdir(ruta)
    for f in archivos:
        if 'oss' in f:
            losfile = f
    return losfile
    
# Using object notation
experiment = st.sidebar.selectbox(
    "Experiments",set(experiments))
st.header(experiment)
cols = st.columns(5)
cases = os.listdir(pth2exp[experiment])
for c in range(len(cases)):
    ppth = os.path.join(pth2exp[experiment],cases[c])
    iloss = floss(ppth)
    cols[0].subheader("Case {}".format(cases[c]))
    cols[0].image(os.path.join(ppth,iloss),use_column_width=True, caption='')
    for i in range(4):
        fn = 'Testing_random_Point-{}.png'.format(i)
        ppth = os.path.join(pth2exp[experiment],cases[c])
        cols[i+1].subheader(':gray[_]')
        cols[i+1].image(os.path.join(ppth,fn),use_column_width=True, caption='')
