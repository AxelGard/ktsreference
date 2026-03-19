

# toList

Returns a new List containing all the elements of this JsArray.

```kotlin
@ExperimentalWasmJsInteropactual inline fun <T> JsArray<T>.toList(): List<T>(source)
```

```kotlin
import kotlin.js.JsArray
import kotlin.js.ExperimentalWasmJsInterop

@OptIn(ExperimentalWasmJsInterop::class)
fun main() {
    // Create a JsArray with some values
    val jsArray: JsArray<String> = js("['apple', 'banana', 'cherry']") as JsArray<String>

    // Convert the JsArray to a Kotlin List
    val list: List<String> = jsArray.toList()

    // Print the resulting list
    console.log(list)   // Output: ["apple", "banana", "cherry"]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/to-list.html)

    