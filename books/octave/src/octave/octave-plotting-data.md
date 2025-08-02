# Plotting data

```
plot(x, y)


% plot one on the othe other
plot(x, y1);
hold on;
plot(x, y2, 'r');  % r means red
xlabel('time')
ylabel('value')
legend('sin', 'cos')
title('my plot')
print -dpng 'myPlot.png'  % save the image
close  % close the current image


% create two separate images
figure(1); plot(x, y1);
figure(2); plot(x, y2);

% two separate graps in the same image
subplot(1, 2, 1); % Divide plot to 1x2 grid and access the 1st element.
plot(x, y1);
subplot(1, 2, 2);
plot(x, y2);
axis([0.5 1 -1 1]) % set the range on the x and y axis
clf;  % clear the figures



imagesc(A)  % visualise the matrix
imagesc(A), colorbar, colormap gray;
imagesc(magic(15)), colorbar, colormap gray;

309671170
a=1, b=2, c=3; % comma-chaining (3 separate commands)
```


