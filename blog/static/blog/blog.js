// Define what happens when the Promise succeeds
function resolvedCallback(data) {
  console.log('Resolved with data ' + data)
}

// Define what happens when the Promise fails
function rejectedCallback(message) {
  console.log('Rejected with message ' + message)
}

// Define the Promise-returning function
const lazyAdd = function(a, b) {
  const doAdd = (resolve, reject) => {
    if (typeof a !== "number" || typeof b !== "number") {
      reject("a and b must both be numbers")
    } else {
      const sum = a + b
      resolve(sum)
    }
  }

  return new Promise(doAdd)
}

// Create and use Promises
const p = lazyAdd(3, 4)
p.then(resolvedCallback, rejectedCallback)

lazyAdd("nan", "alsonan").then(resolvedCallback, rejectedCallback)