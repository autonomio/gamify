// create a range
function range(start, end) {
  var ans = [];
  for (let i = start; i <= end; i++) {
      ans.push(i.toLocaleString('en'));
  }
  return ans;
}

// get average
function avg(a) {
  return a.reduce((a, b) => a + b, 0) / a.length
}

// data loader
function loadData(experiment_id) {
  var filename = '/data/' + experiment_id + '.csv'
  d3.csv(filename).then(generateColumnSelectors);
}

// handle experiment dropdown selection
function experiment_dd(sel) {
  sessionStorage.setItem('experiment_id', String(sel.value))
  loadData(sel.value)
}

function generateExperimentSelector(experiment_ids){
  var experiment = new Vue({
    delimiters: ['||','||'],
    el: '#experiment',
    data: {
      todos: experiment_ids
    }
  })
}

function generateColumnSelectors(dataset) {

  // get the headers
  var keys = Object.keys(dataset[0])

  // populate the left header selector
  var header_dd_left = new Vue({
    delimiters: ['||','||'],
    el: '#header_dd_left',
    data: {
      todos: keys
    }
  })

  // populate the right header selector
  var header_dd_right = new Vue({
    delimiters: ['||','||'],
    el: '#header_dd_right',
    data: {
      todos: keys
    }
  })

  generateData(dataset)

};

function generateData(dataset) {

  // create global for the data
  window.dataset = dataset

  // set the data on default assumption
  label_a = 'val_acc'
  label_b = 'val_loss'

  // set the dropdowns to initial state
  document.getElementById('dd_left').value = label_a
  document.getElementById('dd_right').value = label_b

  // pick the data 
  var a = dataset.map(function(d) {return d[label_a]});
  var b = dataset.map(function(d) {return d[label_b]});

  // update the summaries
  updateSparksA(a, label_a)
  updateSparksB(b, label_b)

  var origin = document.URL.split('/')

  console.log(origin)

 if (origin.slice(-1) == "analyze") {
 	a, b = _scatterData(a, b)
 }

  makeChart(a, b)


};

function _scatterData(a, b) {

	var scatter_a = []
  	var scatter_b = []

	for (let i = 0; i < a.length; i++) {
 		scatter_a.push(Object({"x": a[i], "y": b[i]}));
 		scatter_b.push(Object({"x": a[i], "y": b[i]}));
	}

	return scatter_a, scatter_b

}

// handle initial data data
function initialDataState(experiment_ids) {

  var experiment_id = sessionStorage.getItem('experiment_id')

  if (experiment_id != null){
    // we alerady know what id is selected
    if (experiment_ids.length > 0) {
      loadData(experiment_id)
      document.getElementById('experiment').value = experiment_id
    } else {
      alert("No experiment logs found. Did you pass experiment folder as argument to app.py?")
    }
  
  } else if (experiment_ids.length == 1) {
    // we don't know what id is selected but there is just one
    sessionStorage.setItem('experiment_id', experiment_ids[0])
    document.getElementById('experiment').value = experiment_ids[0]
    loadData(experiment_ids[0])
  
  } else if (experiment_ids.length == 0) {
    // there are no ids
    alert("No experiment logs found. Did you pass experiment folder as argument to app.py?")
  
  } else {
    // there are more than one id (the most recently modified is picked)
    sessionStorage.setItem('experiment_id', experiment_ids[0])
    document.getElementById('experiment').value = experiment_ids[0]
    loadData(experiment_ids[0])

  }
}