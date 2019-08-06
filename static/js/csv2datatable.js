d3.csv(path_to_file).then(prepData);

  function prepData(dataset) {

      // create the columns

      var keys = Object.keys(dataset[0])
      var headers = []

      keys.forEach(item => headers.push(Object({"title": item, "sTitle": item})));

      // create the data

      data = []
      dataset.forEach(row => data.push(Object.values(row)));

      // create the DataTables.js

      $(document).ready(function() {
      $('#example').DataTable( {
          data: data,
          columns: headers
          // set any additional config here
      });
    });
  }
