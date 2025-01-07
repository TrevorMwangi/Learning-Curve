const arr = [5,2,7,1,9,3,4,6,8,10];

function delayedSort(arr) {
    const sorted = [...arr].sort((a,b) => a-b);
    sorted.forEach ((num,index) => {
        setTimeout(( ) => console.log(num), index * 500);
    });
}
delayedSort(arr);