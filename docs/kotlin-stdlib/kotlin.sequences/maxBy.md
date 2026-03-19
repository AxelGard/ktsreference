

# maxBy

Returns the first element yielding the largest value of the given selector function.

```kotlin
@JvmName(name = "maxByOrThrow")inline fun <T, R : Comparable<R>> Sequence<T>.maxBy(selector: (T) -> R): T(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = sequenceOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
)

val oldest = people.maxBy { it.age }

println(oldest)  // Person(name=Charlie, age=35)
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/max-by.html)

    