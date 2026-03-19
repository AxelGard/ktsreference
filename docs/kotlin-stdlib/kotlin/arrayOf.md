

# arrayOf

Returns an array containing the specified elements.

```kotlin
expect inline fun <T> arrayOf(vararg elements: T): Array<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5)
    val names   = arrayOf("Alice", "Bob", "Charlie")

    println(numbers.joinToString(", "))   // 1, 2, 3, 4, 5
    println(names[0])                    // Alice
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/array-of.html)

    