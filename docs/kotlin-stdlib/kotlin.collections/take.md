

# take

Returns a list containing first n elements.

```kotlin
fun <T> Array<out T>.take(n: Int): List<T>(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5, 6)
val firstThree = numbers.take(3)
println(firstThree)  // Output: [1, 2, 3]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/take.html)

    