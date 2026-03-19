

# component3

Returns 3rd element from the array.

```kotlin
inline operator fun <T> Array<out T>.component3(): T(source)
```

```kotlin
fun main() {
    val numbers = arrayOf(10, 20, 30, 40)
    val third = numbers.component3()   // access the third element
    println(third)                     // prints: 30
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/component3.html)

    