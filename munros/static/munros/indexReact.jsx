var MunroComponent = React.createClass({
  render: function () {
    var testStyle = { fontSize: '18px', marginRight: '20px'};
    return(
        <div style={testStyle}>
          We have some react going!
        </div>

      )
  }
});

React.render(
  <MunroComponent />,
  document.getElementById('content')
  )