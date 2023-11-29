import streamlit as st
import os
import re
st.set_page_config(
    page_title="Coastal Hazard Transfer Functions  Project", page_icon=" 🌊",layout="wide" )


## https://tsunamitransferfunctionstest.streamlit.app/

st.title("Hazard Curves Model's Results")

Ms = ['MLP_with_anchor_input','MLP_without_anchor_input',
        'VAE_with_anchor_input','VAE_without_anchor_input',
        'Enc_with_anchor_input','Enc_without_anchor_input']

description={Ms[0]: 'Multilayer perceptron with an onshore hazard curve as input',
             Ms[1]: 'Multilayer perceptron',
             Ms[2]: 'Variational Autoencoder with an onshore hazard curve as input',
             Ms[3]: 'Variational Autoencoder',
             Ms[4]: 'Neural Network Operator with an onshore hazard curve as input',
             Ms[5]: 'Neural Network Operator'
             }

equation={Ms[0]: r'''\textbf{h}=\mathcal{F}(\textbf{Ho},So,s,h_{975} ;\Theta)''',
             Ms[1]: r'''\textbf{h}=\mathcal{F}(\textbf{Ho},So,s ;\Theta)''',
             Ms[2]: r'''\mathcal{N}(\mu,\,\sigma^{2}) = \mathcal{E}(Ho,So,s,h_{975};\Theta) \\ \textbf{h}=\mathcal{D}(\mathcal{N} (\mu,\,\sigma^{2}) ;\Theta)''',
             Ms[3]: r'''\mathcal{N}(\mu,\,\sigma^{2}) = \mathcal{E}(Ho,So,s;\Theta) \\ \textbf{h}=\mathcal{D}(\mathcal{N} (\mu,\,\sigma^{2}) ;\Theta)''',
             Ms[4]: r'''\mathcal{T} = \mathcal{F}(So,s,h_5 ;\Theta) \\ \textbf{h} = \mathcal{T} \odot Ho''',
             Ms[5]: r'''\mathcal{T} = \mathcal{F}(So,s,h_5 ;\Theta) \\ \textbf{h} = \mathcal{T} \odot Ho'''
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
st.header(description[experiment])
st.latex(equation[experiment])
cols = st.columns(5)

cases = os.listdir(pth2exp[experiment])
# To get the folders in the right order
def zorder(text):
    d = re.findall(r'\d+',text)
    return int(d[0])
cases.sort(key=zorder)

for c in range(len(cases)):
    ppth = os.path.join(pth2exp[experiment],cases[c])
    iloss = floss(ppth)
    cols[0].subheader("Case {}".format(cases[c]))
    cols[0].image(os.path.join(ppth,iloss),use_column_width=True, caption='')
    for i in range(4):
        fn = 'Testing_random_Point-{}.png'.format(i)
        ppth = os.path.join(pth2exp[experiment],cases[c])
        cols[i+1].subheader(':blue[{}]'.format(i+1))
        cols[i+1].image(os.path.join(ppth,fn),use_column_width=True, caption='')
