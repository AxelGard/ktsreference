

# toArray

Returns a new Array containing all the elements of this JsArray.

```kotlin
@ExperimentalWasmJsInteropactual inline fun <T> JsArray<T>.toArray(): Array<T>(source)
```

```kotlin
import kotlin.js.JsArray

@OptIn(ExperimentalWasmJsInterop::class)
fun main() {
    // Create a JavaScript array with numbers 1 to 3
    val jsArray: JsArray<Int> = js("[1, 2, 3]")
    // Convert the JsArray to a Kotlin Array
    val kotlinArray: Array<Int> = jsArray.toArray()
    // Print the Kotlin array elements
    kotlinArray.forEach { println(it) }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/to-array.html)

    