

# toJsArray

Returns a new JsArray containing all the elements of this Array.

```kotlin
@ExperimentalWasmJsInteropactual inline fun <T> Array<T>.toJsArray(): JsArray<T>(source)
```

```kotlin
import kotlin.js.*

@ExperimentalWasmJsInterop
fun main() {
    // Kotlin Array
    val kotlinArray = arrayOf(10, 20, 30, 40)

    // Convert to JsArray
    val jsArray: JsArray<Int> = kotlinArray.toJsArray()

    // Access elements and properties via JavaScript interop
    console.log("First element: ${jsArray[0]}")
    console.log("Length: ${jsArray.length}")

    // Iterate with forEach
    jsArray.forEach { element ->
        console.log("Element: $element")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.js/to-js-array.html)

    