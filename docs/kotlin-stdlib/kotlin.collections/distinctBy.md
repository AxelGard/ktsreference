

# distinctBy

Returns a list containing only elements from the given array having distinct keys returned by the given selector function.

```kotlin
inline fun <T, K> Array<out T>.distinctBy(selector: (T) -> K): List<T>(source)
```

```kotlin
data class Person(val name: String, val age: Int)

val people = arrayOf(
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 30),
    Person("David", 25)
)

val uniqueByAge = people.distinctBy { it.age }
println(uniqueByAge)  // [Person(name=Alice, age=30), Person(name=Bob, age=25)]
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/distinct-by.html)

    