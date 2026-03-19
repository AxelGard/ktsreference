

# firstOrNull

Returns the first element, or null if the array is empty.

```kotlin
fun <T> Array<out T>.firstOrNull(): T?(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30)
    val firstNumber = numbers.firstOrNull()
    println(firstNumber)   // 10

    val emptyArray = arrayOf<String>()
    val firstEmpty = emptyArray.firstOrNull()
    println(firstEmpty)    // null
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/first-or-null.html)

    