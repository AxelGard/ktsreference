

# min

Returns the smallest element.

```kotlin
@JvmName(name = "minOrThrow")fun Array<out Double>.min(): Double(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(3.0, 1.5, 2.7, 4.4)
    val smallest = numbers.min()   // uses the minOrThrow extension
    println("The smallest number is $smallest")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/min.html)

    