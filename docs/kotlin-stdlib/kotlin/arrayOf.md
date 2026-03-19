

# arrayOf

Returns an array containing the specified elements.

```kotlin
expect inline fun <T> arrayOf(vararg elements: T): Array<T>(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30)
    val words = arrayOf("foo", "bar", "baz")
    println(numbers.joinToString()) // prints: 10, 20, 30
    println(words.joinToString())   // prints: foo, bar, baz
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/array-of.html)

    