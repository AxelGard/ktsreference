

# arrayOf

 [kotlin-stdlib](/kotlin-stdlib) / [kotlin](/kotlin-stdlib/kotlin) / [arrayOf](kotlin-stdlib/kotlin/arrayOf)

Returns an array containing the specified elements.

```kotlin
expect inline fun <T> arrayOf(vararg elements: T): Array<T>(source)
```

```kotlin
fun main() {
    val ints = arrayOf(1, 2, 3, 4, 5)
    val strings = arrayOf("apple", "banana", "cherry")

    println(ints.joinToString())   // Output: 1, 2, 3, 4, 5
    println(strings.joinToString()) // Output: apple, banana, cherry
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/array-of.html)

    