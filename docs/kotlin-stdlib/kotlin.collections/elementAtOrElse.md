

# elementAtOrElse

Returns an element at the given index or the result of calling the defaultValue function if the index is out of bounds of this array.

```kotlin
inline fun <T> Array<out T>.elementAtOrElse(index: Int, defaultValue: (Int) -> T): T(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30)

    val value = numbers.elementAtOrElse(5) { idx ->
        "No element at index $idx, using default"
    }

    println(value)  // prints: No element at index 5, using default
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/element-at-or-else.html)

    