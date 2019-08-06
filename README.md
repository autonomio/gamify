<h1 align="center">
  <br>
  <a href="http://autonom.io"><img src="https://i.ibb.co/qBsYDf3/gamify-logo.png" alt="Gamify" width="150"></a>
  <br>
</h1>

<p align="center">
  
  <a href="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png">
    <img width=150px src="https://raw.githubusercontent.com/eka-foundation/home/master/images/by-sa.png" alt="License">
  </a>

</p>

<p align="center">
  <a href="#Gamify">Gamify</a> •
  <a href="#Key-Features">Key Features</a> •
  <a href="#Install-and-Use">Install and Use</a> •
  <a href="#Support">Support</a> •
  <a href="https://github.com/autonomio/talos/issues">Issues</a> •
  <a href="#License">License</a> •
  <a href="https://github.com/autonomio/gamify/archive/master.zip">Download</a>
</p>
<hr>
<p align="center">
  
Gamify puts the researcher back in the driver's seat in modern deep learning workflow by unlocking a new era of man-machine symbiosis in artificial intelligence model development. As the mission matures, developing state-of-the-art deep learning models will feel more like playing a Real-Time Strategy Game. 
</p>

<p align="center">
<img src='https://i.ibb.co/88SKWSg/overview.png' width=550px>
</p>

### Gamify

TL;DR

Gamify radically changes the hyperparameter optimization workflow by giving the researcher powerful tools to analyze, control, and optimize the process during the experiment. Gamify is an add-on to leading hyperparameter scanning solution [Talos](http://github.com/autonomio/talos). Talos exposes Keras functionality entirely and there is no new syntax or templates to learn. 

<hr>

### :wrench: Key Features

Gamify adds a visual command center to [Talos](http://github.com/autonomio/talos) experiments.

- Analyze experiment log
- Visualize experiment results
- Monitor and analyze epoch-by-epoch training performance
- Make changes in real-time to the experiment (coming soon)

Gamify works on **Linux, Mac OSX**, and **Windows**.

<hr>

### 📈 Examples

#### Track epoch-by-epoch progress

<img src="https://i.ibb.co/HTsZdXC/analyze.png" width=550px>

#### Analyze the results

<img src="https://i.ibb.co/88SKWSg/overview.png" width=550px>

#### Analyze the experiment log

<img src="https://i.ibb.co/mvBTQN1/experiment-log.png" width=550px>



<hr>

### 💾 Install and Use

Download the repo, navigate to the `/gamify` folder (or add `gamify.py` to your PATH) and: 

`python gamify.app /path/to/talos/experiment`

Here `/path/to/talos/experiment` refers to the folder Talos creates based on `Scan(...experiment_name...)` from v0.6.2 onwards.

Note, the live updating epoch-by-epoch monitor requires the use of `ExperimentLogCallback` in Talos. Which means that your input model `model.fit` would like this: 

```
out = model.fit(...
                callbacks=[talos.utils.ExperimentLogCallback('minimal_iris', params)],
                 ...)
```
<hr>

### 💬 How to get Support

You can use the regular Talos support channels for Gamify.

| I want to...                     | Go to...                                                  |
| -------------------------------- | ---------------------------------------------------------- |
| **...troubleshoot**           | [Docs] · [Wiki] · [GitHub Issue Tracker]                   |
| **...report a bug**           | [GitHub Issue Tracker]                                     |
| **...suggest a new feature**  | [GitHub Issue Tracker]                                     |
| **...get support**            | [Stack Overflow] · [Spectrum Chat]                         |
| **...have a discussion**      | [Spectrum Chat]                                            |

[github issue tracker]: https://github.com/automio/talos/issues
[docs]: https://autonomio.github.io/talos/
[wiki]: https://github.com/autonomio/talos/wiki
[stack overflow]: https://stackoverflow.com/questions/tagged/talos
[spectrum chat]: https://spectrum.chat/talos

<hr>

### 📢 Citations

If you use Gamify for published work, please cite:

`Autonomio Gamify [Computer software]. (2019). Retrieved from http://github.com/autonomio/gamify.`

<hr>

### 📃 License

[CC SA](https://creativecommons.org/licenses/by-sa/4.0/legalcode)
