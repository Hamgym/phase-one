// 開啟選單
const burger = document.querySelector("#burger");
const list = document.querySelector(".menu ol");
burger.addEventListener("click", openList);
function openList() {
  list.setAttribute("class", "open");
}

// 關閉選單
const cross = document.querySelector("#cross");
cross.addEventListener("click", closeList);
function closeList() {
  list.setAttribute("class", "");
}

// 取得所有資料
let allData;
async function getData() {
  const url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const json = await response.json();
    const spots = json.data.results;

    let data = [];
    for (let spot of spots) {
      let row = [];
      row.push(spot["stitle"]);
      let list = spot["filelist"];
      let end = list.indexOf("https", 5);
      list = list.slice(0, end);
      row.push(list);
      data.push([...row]);
    }

    allData = data;
    return data;

  } catch (error) {
    console.error(error.message);
  }
}

// 改變promotion欄位內容
function changePro(data) {
  for (let i = 0; i < 3; i++) {
    let target = `#pm${i + 1}`
    let pro = document.querySelector(target)
    pro.children[0].src = data[i][1];
    const para = document.createElement("p");
    para.innerText = data[i][0];
    pro.children[1].remove();
    pro.appendChild(para);
  }
}

// 改變product欄位內容
function changePd(data) {
  let product = document.querySelector(".product");
  let pds = product.children;
  for (let i = 0; i < pds.length; i++) {
    pds[i].children[1].src = data[i + 3][1];
    const para = document.createElement("p");
    para.innerText = data[i + 3][0];
    pds[i].children[2].remove();
    pds[i].appendChild(para);
  }
}

// 載入後執行一次
(async function () {
  await getData();  // 取得 allData
  changePro(allData);
  changePd(allData);
})();

// 載入更多product
let more = document.querySelector(".more");
more.addEventListener("click", showMore);
function showMore() {
  let data = allData;
  let product = document.querySelector(".product");
  let children = product.children;

  for (let i = 0; i < 10; i++) {
    if (children.length >= data.length - 3) {
      break;
    }
    let clone = children[i].cloneNode(true);
    product.appendChild(clone);
  }

  changePd(data);
}