

# ifEmpty

Returns this array if it's not empty or the result of calling defaultValue function if the array is empty.

```kotlin
inline fun <C : Array<*>, R, R> C.ifEmpty(defaultValue: () -> R): R(source)
```

```kotlin
fun main() {
    // Example with a non‑empty array
    val nonEmpty = arrayOf(1, 2, 3)
    val result1 = nonEmpty.ifEmpty { "default value" } // returns the array itself
    println(result1)   // prints: [1, 2, 3]

    // Example with an empty array
    val empty = emptyArray<Int>()
    val result2 = empty.ifEmpty { "default value" }   // returns the default value
    println(result2)   // prints: default value
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/if-empty.html)

    