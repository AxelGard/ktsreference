

# component4

Returns 4th element from the array.

```kotlin
inline operator fun <T> Array<out T>.component4(): T(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30, 40, 50)
    val fourthNumber = numbers.component4()
    println("The 4th element is $fourthNumber")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/component4.html)

    