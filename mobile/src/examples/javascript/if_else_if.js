var i = 10;

while (true) {
  console.log(i);
  i++;
  if (i <= 14) {
    console.log('kid')
  } else if (i < 18) {
    console.log('high school');
  } else {
    console.log('too big');
     break;
  }
}
